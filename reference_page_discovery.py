#!/usr/bin/env python3
"""
统一测试所有交易所的文档页面数量
用法:
  python3 test_all_exchanges.py              # 测试所有交易所
  python3 test_all_exchanges.py binance     # 只测试指定交易所
"""
import subprocess
import json
import time
import sys
from typing import List, Dict, Tuple
from loguru import logger as log


def run_browser_command(session: str, *args, timeout: int = 10, verbose: bool = False) -> dict:
    """运行 agent-browser 命令并返回结果"""
    cmd = ['agent-browser', '--session', session] + list(args)

    if verbose:
        log.info(f"执行命令: {' '.join(cmd[:5])}...")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if '--json' in args:
            data = json.loads(result.stdout)
            if verbose:
                log.info(f"命令成功,返回数据类型: {type(data.get('data', {}).get('result'))}")
            return data
        return {'success': True, 'stdout': result.stdout}
    except subprocess.TimeoutExpired:
        log.error(f"❌ 命令超时")
        return {'success': False, 'error': 'timeout'}
    except json.JSONDecodeError:
        log.error(f"❌ JSON解析失败")
        return {'success': False, 'error': 'json_decode'}
    except Exception as e:
        log.error(f"❌ 命令失败: {e}")
        return {'success': False, 'error': str(e)}


def expand_docusaurus_menu(session: str, link_selector: str = 'a[role="button"]', max_iterations: int = 50) -> int:
    """
    展开 Docusaurus 风格的折叠菜单

    Args:
        session: browser session
        link_selector: 折叠菜单内的链接选择器 (a[role="button"] 或 a[href="#"])
        max_iterations: 最大迭代次数

    Returns:
        迭代次数
    """
    last_link_count = 0

    for i in range(max_iterations):
        # 点击所有折叠菜单
        js_expand = f'''
        const collapsed = document.querySelectorAll('.menu__list-item--collapsed');
        let clicked = 0;
        collapsed.forEach(item => {{
            const link = item.querySelector('{link_selector}');
            if (link) {{
                try {{ link.click(); clicked++; }} catch(e) {{}}
            }}
        }});
        clicked;
        '''

        result_expand = run_browser_command(session, 'eval', js_expand, '--json')
        clicked = 0
        if result_expand.get('success') is not False:
            try:
                clicked = result_expand['data']['result']
            except:
                pass

        if clicked == 0:
            print(f"  ✓ 没有更多折叠菜单")
            break

        time.sleep(0.3)  # 等待DOM更新

        # 统计点击后的链接数
        js_count = 'document.querySelectorAll(".menu__link").length'
        result = run_browser_command(session, 'eval', js_count, '--json')

        link_count = 0
        if result.get('success') is not False:
            try:
                link_count = result['data']['result']
            except:
                pass

        # 检查是否有增长
        if link_count == last_link_count and last_link_count > 0:
            print(f"  ✓ 链接数无增长，都是空菜单，停止展开")
            break

        delta = link_count - last_link_count if last_link_count > 0 else link_count
        if delta > 0:
            print(f"  [轮次 {i+1}] 点击 {clicked} 个折叠，链接增加 {delta} → 总计 {link_count}")

        last_link_count = link_count

    return i + 1


def extract_links(session: str, selector: str) -> List[str]:
    """提取所有链接"""
    js = f'''
    Array.from(document.querySelectorAll('{selector}'))
        .map(a => a.href)
        .filter(href => href && !href.endsWith('#'))
    '''

    result = run_browser_command(session, 'eval', js, '--json')

    if result.get('success') is False:
        return []

    try:
        links = result['data']['result']
        if isinstance(links, list):
            return list(set(links))  # 去重
    except:
        pass

    return []


def test_binance() -> Dict[str, int]:
    """测试币安的所有金融交易产品"""
    log.info("\n" + "="*60)
    log.info("开始测试 Binance")
    log.info("="*60)
    session = 'test-binance'

    # 打开币安首页获取产品列表
    homepage = "https://developers.binance.com/docs/zh-CN/derivatives/Introduction"
    log.info(f"打开币安首页: {homepage}")
    run_browser_command(session, 'open', homepage, timeout=15)
    log.info("等待页面加载...")
    time.sleep(3)

    # 步骤1: 点击产品选择器按钮
    log.info("点击产品选择器...")
    js_click_btn = 'document.querySelector("button[class*=\\"productSelector\\"]").click(); 1'
    run_browser_command(session, 'eval', js_click_btn, '--json')
    time.sleep(1)

    # 步骤2: 获取产品列表（前10个是金融交易核心产品）
    log.info("获取金融交易产品（前10个）...")
    js_get_products = '''
    const products = [];
    const productItems = document.querySelectorAll('a[class*="productItem"]');

    // 只取前10个产品（金融交易分类）
    const items = Array.from(productItems).slice(0, 10);

    items.forEach(item => {
        const titleEl = item.querySelector('[class*="Title"]');
        const title = titleEl ? titleEl.textContent.trim() : '';
        const href = item.href;

        if (title && href) {
            products.push({ name: title, url: href });
        }
    });

    products;
    '''

    result = run_browser_command(session, 'eval', js_get_products, '--json')
    products = []

    if result.get('success') is not False:
        try:
            products = result['data']['result']
        except:
            pass

    if not products:
        print("  ❌ 无法获取产品列表")
        run_browser_command(session, 'close')
        return {}

    print(f"  发现 {len(products)} 个产品")

    # 测试每个产品
    product_counts = {}

    for product in products:
        name = product['name']
        url = product['url']
        print(f"\n  测试产品: {name}")

        run_browser_command(session, 'open', url, timeout=15)
        time.sleep(3)

        # 展开菜单 - Binance 使用 a[role="button"] 选择器
        expand_docusaurus_menu(session, link_selector='a[role="button"]')

        # 提取链接
        links = extract_links(session, '.menu__link:not([role="button"])')
        product_counts[name] = len(links)
        print(f"  {name}: {len(links)} 个页面")

    run_browser_command(session, 'close')
    return product_counts


def test_bybit() -> int:
    """测试 Bybit"""
    print("\n测试 Bybit...")
    session = 'test-bybit'

    url = "https://bybit-exchange.github.io/docs/v5/guide"
    run_browser_command(session, 'open', url, timeout=15)
    time.sleep(3)

    # 展开菜单 - Bybit 使用 a[href="#"] 选择器
    expand_docusaurus_menu(session, link_selector='a[href="#"]')

    # 提取链接
    links = extract_links(session, '.menu__link:not([href="#"])')
    count = len(links)
    print(f"  发现 {count} 个页面")

    run_browser_command(session, 'close')
    return count


def test_okx() -> int:
    """测试 OKX (SPA 架构)"""
    print("\n测试 OKX...")
    session = 'test-okx'

    url = "https://www.okx.com/docs-v5/zh/#overview"
    run_browser_command(session, 'open', url, timeout=15)
    time.sleep(3)

    # OKX 是 SPA,需要提取锚点链接
    js = '''
    Array.from(document.querySelectorAll('a[href*="#"]'))
        .map(a => a.href)
        .filter(href => href && href.includes('#') && !href.endsWith('#'))
    '''

    result = run_browser_command(session, 'eval', js, '--json')
    links = []

    if result.get('success') is not False:
        try:
            links = result['data']['result']
            links = list(set(links))  # 去重
        except:
            pass

    count = len(links)
    print(f"  发现 {count} 个页面")

    run_browser_command(session, 'close')
    return count


def test_coinbase() -> int:
    """测试 Coinbase Exchange API"""
    print("\n测试 Coinbase Exchange API...")
    session = 'test-coinbase'

    # 打开任意一个页面即可（三个section共享侧边栏）
    url = 'https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/introduction'
    run_browser_command(session, 'open', url, timeout=15)
    time.sleep(3)

    # 展开所有按钮
    last_link_count = 0

    for i in range(15):
        # 点击所有折叠按钮
        js_expand = '''
        const buttons = document.querySelectorAll('button[aria-expanded="false"]');
        let clicked = 0;
        buttons.forEach(btn => {
            try {
                btn.click();
                clicked++;
            } catch(e) {}
        });
        clicked;
        '''

        result_expand = run_browser_command(session, 'eval', js_expand, '--json')
        clicked = 0
        if result_expand.get('success') is not False:
            try:
                clicked = result_expand['data']['result']
            except:
                pass

        if clicked == 0:
            print(f"  ✓ 没有更多折叠按钮")
            break

        time.sleep(0.3)

        # 统计链接数
        js_count = 'document.querySelectorAll("#navigation-items a, #sidebar-group a").length'
        result = run_browser_command(session, 'eval', js_count, '--json')

        link_count = 0
        if result.get('success') is not False:
            try:
                link_count = result['data']['result']
            except:
                pass

        if link_count == last_link_count and last_link_count > 0:
            print(f"  ✓ 链接数无增长，停止展开")
            break

        delta = link_count - last_link_count if last_link_count > 0 else link_count
        if delta > 0:
            print(f"  [轮次 {i+1}] 点击 {clicked} 个按钮，链接增加 {delta} → 总计 {link_count}")

        last_link_count = link_count

    # 提取所有链接
    js_links = '''
    Array.from(document.querySelectorAll('#navigation-items a, #sidebar-group a'))
        .map(a => a.href)
        .filter(href => href && !href.endsWith('#'))
    '''

    result_links = run_browser_command(session, 'eval', js_links, '--json')
    links = []

    if result_links.get('success') is not False:
        try:
            links = result_links['data']['result']
            links = list(set(links))  # 去重
        except:
            pass

    count = len(links)
    print(f"  发现 {count} 个页面")

    run_browser_command(session, 'close')
    return count


def test_kraken() -> Dict[str, int]:
    """测试 Kraken (5个navbar产品)"""
    print("\n测试 Kraken...")
    session = 'test-kraken'

    # 打开首页获取navbar产品
    url = "https://docs.kraken.com/api/"
    run_browser_command(session, 'open', url, timeout=15)
    time.sleep(3)

    # 获取navbar中 Exchange 分类下的产品链接
    js_products = '''
    (function() {
        const dropdowns = Array.from(document.querySelectorAll('.navbar__item.dropdown'));
        const exchangeDropdown = dropdowns.find(item => {
            const title = item.querySelector('.navbar__link')?.textContent.trim();
            return title === 'Exchange';
        });

        if (!exchangeDropdown) return [];

        return Array.from(exchangeDropdown.querySelectorAll('a.dropdown__link'))
            .map(a => ({
                name: a.textContent.trim(),
                url: a.href
            }))
            .filter(p => p.name && p.url);
    })()
    '''

    result = run_browser_command(session, 'eval', js_products, '--json')
    products = []

    if result.get('success') is not False:
        try:
            products = result['data']['result']
        except:
            pass

    if not products:
        print("  ❌ 无法获取产品列表")
        run_browser_command(session, 'close')
        return {}

    print(f"  发现 {len(products)} 个产品")

    product_counts = {}

    for product in products:
        name = product['name']
        url = product['url']
        print(f"\n  测试产品: {name}")

        run_browser_command(session, 'open', url, timeout=15)
        time.sleep(2)

        # 提取侧边栏链接
        js_links = '''
        Array.from(document.querySelectorAll('.menu__link'))
            .map(a => a.href)
            .filter(href => href && !href.endsWith('#'))
        '''

        result_links = run_browser_command(session, 'eval', js_links, '--json')
        links = []

        if result_links.get('success') is not False:
            try:
                links = result_links['data']['result']
                links = list(set(links))  # 去重
            except:
                pass

        count = len(links)
        product_counts[name] = count
        print(f"    {name}: {count} 个页面")

    run_browser_command(session, 'close')
    return product_counts


def test_gateio() -> int:
    """测试 Gate.io (SPA架构)"""
    print("\n测试 Gate.io...")
    session = 'test-gateio'

    url = "https://www.gate.io/docs/developers/apiv4/zh_CN/"
    run_browser_command(session, 'open', url, timeout=15)
    time.sleep(3)

    # Gate.io 是 SPA,提取锚点链接
    js = '''
    Array.from(document.querySelectorAll('a[href*="#"]'))
        .map(a => a.href)
        .filter(href => href && href.includes('#') && !href.endsWith('#'))
    '''

    result = run_browser_command(session, 'eval', js, '--json')
    links = []

    if result.get('success') is not False:
        try:
            links = result['data']['result']
            links = list(set(links))  # 去重
        except:
            pass

    count = len(links)
    print(f"  发现 {count} 个页面")

    run_browser_command(session, 'close')
    return count


def test_hyperliquid() -> int:
    """测试 Hyperliquid"""
    print("\n测试 Hyperliquid...")
    session = 'test-hyperliquid'

    url = "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api"
    run_browser_command(session, 'open', url, timeout=15)
    time.sleep(3)

    # 提取所有文档链接
    js = '''
    Array.from(document.querySelectorAll('a[href*="/for-developers/api"]'))
        .map(a => a.href)
        .filter(href => href && !href.endsWith('#'))
    '''

    result = run_browser_command(session, 'eval', js, '--json')
    links = []

    if result.get('success') is not False:
        try:
            links = result['data']['result']
            links = list(set(links))  # 去重
        except:
            pass

    count = len(links)
    print(f"  发现 {count} 个页面")

    run_browser_command(session, 'close')
    return count


def main():
    log.info("=" * 60)
    log.info("交易所文档页面统计")
    log.info("=" * 60)

    # 检查命令行参数
    exchanges_to_test = []
    if len(sys.argv) > 1:
        exchanges_to_test = [arg.lower() for arg in sys.argv[1:]]
        log.info(f"只测试指定交易所: {', '.join(exchanges_to_test)}")
    else:
        exchanges_to_test = ['binance', 'bybit', 'okx', 'coinbase', 'kraken', 'gateio', 'hyperliquid']
        log.info("测试所有交易所")

    results = {}

    # 测试各个交易所
    if 'binance' in exchanges_to_test:
        try:
            results['Binance'] = test_binance()
        except Exception as e:
            log.error(f"❌ Binance 测试失败: {e}")
            results['Binance'] = {}

    if 'bybit' in exchanges_to_test:
        try:
            results['Bybit'] = test_bybit()
        except Exception as e:
            log.error(f"❌ Bybit 测试失败: {e}")
            results['Bybit'] = 0

    if 'okx' in exchanges_to_test:
        try:
            results['OKX'] = test_okx()
        except Exception as e:
            log.error(f"❌ OKX 测试失败: {e}")
            results['OKX'] = 0

    if 'coinbase' in exchanges_to_test:
        try:
            results['Coinbase'] = test_coinbase()
        except Exception as e:
            log.error(f"❌ Coinbase 测试失败: {e}")
            results['Coinbase'] = 0

    if 'kraken' in exchanges_to_test:
        try:
            results['Kraken'] = test_kraken()
        except Exception as e:
            log.error(f"❌ Kraken 测试失败: {e}")
            results['Kraken'] = {}

    if 'gateio' in exchanges_to_test:
        try:
            results['Gate.io'] = test_gateio()
        except Exception as e:
            log.error(f"❌ Gate.io 测试失败: {e}")
            results['Gate.io'] = 0

    if 'hyperliquid' in exchanges_to_test:
        try:
            results['Hyperliquid'] = test_hyperliquid()
        except Exception as e:
            log.error(f"❌ Hyperliquid 测试失败: {e}")
            results['Hyperliquid'] = 0

    # 输出汇总
    print("\n" + "=" * 60)
    print("汇总结果")
    print("=" * 60)

    total = 0

    # Binance
    if isinstance(results.get('Binance'), dict):
        binance_total = sum(results['Binance'].values())
        print(f"\nBinance (金融交易):")
        for product, count in results['Binance'].items():
            print(f"  - {product}: {count} 页")
        print(f"  小计: {binance_total} 页")
        total += binance_total

    # Bybit
    if isinstance(results.get('Bybit'), int):
        print(f"\nBybit: {results['Bybit']} 页")
        total += results['Bybit']

    # OKX
    if isinstance(results.get('OKX'), int):
        print(f"\nOKX: {results['OKX']} 页")
        total += results['OKX']

    # Coinbase
    if isinstance(results.get('Coinbase'), int):
        print(f"\nCoinbase Exchange: {results['Coinbase']} 页")
        total += results['Coinbase']

    # Kraken
    if isinstance(results.get('Kraken'), dict):
        kraken_total = sum(results['Kraken'].values())
        print(f"\nKraken:")
        for product, count in results['Kraken'].items():
            print(f"  - {product}: {count} 页")
        print(f"  小计: {kraken_total} 页")
        total += kraken_total

    # Gate.io
    if isinstance(results.get('Gate.io'), int):
        print(f"\nGate.io: {results['Gate.io']} 页")
        total += results['Gate.io']

    # Hyperliquid
    if isinstance(results.get('Hyperliquid'), int):
        print(f"\nHyperliquid: {results['Hyperliquid']} 页")
        total += results['Hyperliquid']

    print(f"\n{'=' * 60}")
    print(f"总计: {total} 页")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
