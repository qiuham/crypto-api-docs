---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/appendix
api_type: REST
updated_at: 2026-01-15T23:49:46.718667
---

# Appendix

## Name restrictions[​](/docs/wallet/travel-rule/appendix#name-restrictions "Direct link to Name restrictions")

Strings that match the following regular expression rules are accepted.
    
    
    REGEXP : ^(?=.{1,})(?!.{100,})(?!.*([a-zA-Z])\1{2,})(?!.*[0-9!@#$%^&*()_=.~`<>/:;?€£¥₹₩¢₿+=÷]).*$  
    

  * The string length must be between 1 and 99 characters, inclusive.
  * The string must not contain any digits or a specified set of special characters.
  * The string must not contain any letter repeated consecutively 3 or more times.
  * The string may contain letters (both uppercase and lowercase) and other characters that are not excluded (such as spaces, punctuation marks not listed in the excluded symbols, etc.).



## Country (Regions) ISO code[​](/docs/wallet/travel-rule/appendix#country-regions-iso-code "Direct link to Country \(Regions\) ISO code")

> You will not be able to use an ISO code that is not listed in the table

Country (Regions)| Code  
---|---  
Afghanistan| af  
Albania| al  
Algeria| dz  
American Samoa| as  
Andorra| ad  
Angola| ao  
Anguilla| ai  
Antigua and Barbuda| ag  
Argentina| ar  
Armenia| am  
Aruba| aw  
Australia| au  
Austria| at  
Azerbaijan| az  
Bahamas (the)| bs  
Bahrain| bh  
Bangladesh| bd  
Barbados| bb  
Belarus| by  
Belgium| be  
Belize| bz  
Benin| bj  
Bermuda| bm  
Bhutan| bt  
Bolivia (Plurinational State of)| bo  
Bonaire, Sint Eustatius and Saba| bq  
Bosnia and Herzegovina| ba  
Botswana| bw  
Bouvet Island| bv  
Brazil| br  
British Indian Ocean Territory (the)| io  
Brunei Darussalam| bn  
Bulgaria| bg  
Burkina Faso| bf  
Burundi| bi  
Cabo Verde| cv  
Cambodia| kh  
Cameroon| cm  
Canada| ca  
Cayman Islands (the)| ky  
Central African Republic (the)| cf  
Chad| td  
Chile| cl  
China| cn  
Christmas Island| cx  
Cocos (Keeling) Islands (the)| cc  
Colombia| co  
Comoros (the)| km  
Congo (the Democratic Republic of the)| cd  
Congo (the)| cg  
Cook Islands (the)| ck  
Costa Rica| cr  
Croatia| hr  
Cuba| cu  
Curaçao| cw  
Cyprus| cy  
Czechia| cz  
Côte d'Ivoire| ci  
Denmark| dk  
Djibouti| dj  
Dominica| dm  
Dominican Republic (the)| do  
Ecuador| ec  
Egypt| eg  
El Salvador| sv  
Equatorial Guinea| gq  
Eritrea| er  
Estonia| ee  
Eswatini| sz  
Ethiopia| et  
Falkland Islands (the) [Malvinas]| fk  
Faroe Islands (the)| fo  
Fiji| fj  
Finland| fi  
France| fr  
French Guiana| gf  
French Polynesia| pf  
Gabon| ga  
Gambia (the)| gm  
Georgia| ge  
Germany| de  
Ghana| gh  
Gibraltar| gi  
Greece| gr  
Greenland| gl  
Grenada| gd  
Guadeloupe| gp  
Guam| gu  
Guatemala| gt  
Guinea| gn  
Guinea-Bissau| gw  
Guernsey| gg  
Guyana| gy  
Haiti| ht  
Heard Island and McDonald Islands| hm  
Holy See (the)| va  
Honduras| hn  
Hungary| hu  
Iceland| is  
India| in  
Indonesia| id  
Iran (Islamic Republic of)| ir  
Iraq| iq  
Ireland| ie  
Israel| il  
Italy| it  
Jamaica| jm  
Japan| jp  
Jersey| je  
Jordan| jo  
Kazakhstan| kz  
Kenya| ke  
Kiribati| ki  
Korea (the Democratic People's Republic of)| kp  
Korea (the Republic of)| kr  
Kosovo| xk  
Kuwait| kw  
Kyrgyzstan| kg  
Lao People's Democratic Republic (the)| la  
Latvia| lv  
Lebanon| lb  
Lesotho| ls  
Liberia| lr  
Libya| ly  
Liechtenstein| li  
Lithuania| lt  
Luxembourg| lu  
Madagascar| mg  
Malawi| mw  
Malaysia| my  
Maldives| mv  
Mali| ml  
Malta| mt  
Marshall Islands (the)| mh  
Martinique| mq  
Mauritania| mr  
Mauritius| mu  
Mayotte| yt  
Mexico| mx  
Micronesia (Federated States of)| fm  
Moldova (the Republic of)| md  
Monaco| mc  
Mongolia| mn  
Montenegro| me  
Montserrat| ms  
Morocco| ma  
Mozambique| mz  
Myanmar| mm  
Namibia| na  
Nauru| nr  
Nepal| np  
Netherlands (the)| nl  
New Caledonia| nc  
New Zealand| nz  
Nicaragua| ni  
Niger (the)| ne  
Nigeria| ng  
Niue| nu  
Northern Cyprus| cy-2  
Norfolk Island| nf  
Northern Mariana Islands (the)| mp  
Norway| no  
Oman| om  
Pakistan| pk  
Palau| pw  
Palestine, State of| ps  
Panama| pa  
Papua New Guinea| pg  
Paraguay| py  
Peru| pe  
Philippines (the)| ph  
Pitcairn| pn  
Poland| pl  
Portugal| pt  
Pridnestrovian Moldavian Republic| pmr  
Puerto Rico| pr  
Qatar| qa  
Republic of North Macedonia| mk  
Romania| ro  
Russian Federation (the)| ru  
Rwanda| rw  
Réunion| re  
Saint Barthélemy| bl  
Saint Helena, Ascension and Tristan da Cunha| sh  
Saint Kitts and Nevis| kn  
Saint Lucia| lc  
Saint Martin (French part)| mf  
Saint Pierre and Miquelon| pm  
Saint Vincent and the Grenadines| vc  
Samoa| ws  
San Marino| sm  
Sao Tome and Principe| st  
Saudi Arabia| sa  
Senegal| sn  
Serbia| rs  
Seychelles| sc  
Sierra Leone| sl  
Singapore| sg  
Sint Maarten (Dutch part)| sx  
Slovakia| sk  
Slovenia| si  
Solomon Islands| sb  
Somalia| so  
Somaliland, Republic of| so-2  
South Africa| za  
South Georgia and the South Sandwich Islands| gs  
South Ossetia| so-3  
South Sudan| ss  
Spain| es  
Sri Lanka| lk  
Sudan (the)| sd  
Suriname| sr  
Svalbard and Jan Mayen| sj  
Sweden| se  
Switzerland| ch  
Syrian Arab Republic| sy  
Tajikistan| tj  
Tanzania, United Republic of| tz  
Thailand| th  
Timor-Leste| tl  
Togo| tg  
Tokelau| tk  
Tonga| to  
Trinidad and Tobago| tt  
Tunisia| tn  
Turkey| tr  
Turkmenistan| tm  
Turks and Caicos Islands (the)| tc  
Tuvalu| tv  
Uganda| ug  
Ukraine| ua  
United Arab Emirates (the)| ae  
United Kingdom of Great Britain and Northern Ireland (the)| gb  
United States Minor Outlying Islands (the)| um  
United States of America (the)| us  
Uruguay| uy  
Uzbekistan| uz  
Vanuatu| vu  
Venezuela (Bolivarian Republic of)| ve  
Viet Nam| vn  
Virgin Islands (British)| vg  
Virgin Islands (U.S.)| vi  
Wallis and Futuna| wf  
Western Sahara| eh  
Yemen| ye  
Zambia| zm  
Zimbabwe| zw  
Åland Islands| ax

---

# Appendix

## 姓名限制[​](/docs/zh-CN/wallet/travel-rule/appendix#姓名限制 "姓名限制的直接链接")

姓名的字符串需要符合下列的正则表达式才会被接受.
    
    
    ^(?=.{1,})(?!.{100,})(?!.*([a-zA-Z])\1{2,})(?!.*[0-9!@#$%^&*()_=.~`<>/:;?€£¥₹₩¢₿+=÷]).*$  
    

  * 字符串长度必须在1到50个字符之间（含1和50）。
  * 字符串中不能包含数字和指定的一系列特殊符号。
  * 字符串中不能有任何字母连续重复3次或以上。
  * 字符串可以包含字母（大小写均可）和其他未被排除的字符（比如空格、标点符号中未列出的符号等）。



## 国家（地区）ISO编码[​](/docs/zh-CN/wallet/travel-rule/appendix#国家地区iso编码 "国家（地区）ISO编码的直接链接")

> 您将无法使用表中未列出的ISO代码

国家（地区）| 编码  
---|---  
Afghanistan| af  
Albania| al  
Algeria| dz  
American Samoa| as  
Andorra| ad  
Angola| ao  
Anguilla| ai  
Antigua and Barbuda| ag  
Argentina| ar  
Armenia| am  
Aruba| aw  
Australia| au  
Austria| at  
Azerbaijan| az  
Bahamas (the)| bs  
Bahrain| bh  
Bangladesh| bd  
Barbados| bb  
Belarus| by  
Belgium| be  
Belize| bz  
Benin| bj  
Bermuda| bm  
Bhutan| bt  
Bolivia (Plurinational State of)| bo  
Bonaire, Sint Eustatius and Saba| bq  
Bosnia and Herzegovina| ba  
Botswana| bw  
Bouvet Island| bv  
Brazil| br  
British Indian Ocean Territory (the)| io  
Brunei Darussalam| bn  
Bulgaria| bg  
Burkina Faso| bf  
Burundi| bi  
Cabo Verde| cv  
Cambodia| kh  
Cameroon| cm  
Canada| ca  
Cayman Islands (the)| ky  
Central African Republic (the)| cf  
Chad| td  
Chile| cl  
China| cn  
Christmas Island| cx  
Cocos (Keeling) Islands (the)| cc  
Colombia| co  
Comoros (the)| km  
Congo (the Democratic Republic of the)| cd  
Congo (the)| cg  
Cook Islands (the)| ck  
Costa Rica| cr  
Croatia| hr  
Cuba| cu  
Curaçao| cw  
Cyprus| cy  
Czechia| cz  
Côte d'Ivoire| ci  
Denmark| dk  
Djibouti| dj  
Dominica| dm  
Dominican Republic (the)| do  
Ecuador| ec  
Egypt| eg  
El Salvador| sv  
Equatorial Guinea| gq  
Eritrea| er  
Estonia| ee  
Eswatini| sz  
Ethiopia| et  
Falkland Islands (the) [Malvinas]| fk  
Faroe Islands (the)| fo  
Fiji| fj  
Finland| fi  
France| fr  
French Guiana| gf  
French Polynesia| pf  
Gabon| ga  
Gambia (the)| gm  
Georgia| ge  
Germany| de  
Ghana| gh  
Gibraltar| gi  
Greece| gr  
Greenland| gl  
Grenada| gd  
Guadeloupe| gp  
Guam| gu  
Guatemala| gt  
Guinea| gn  
Guinea-Bissau| gw  
Guernsey| gg  
Guyana| gy  
Haiti| ht  
Heard Island and McDonald Islands| hm  
Holy See (the)| va  
Honduras| hn  
Hungary| hu  
Iceland| is  
India| in  
Indonesia| id  
Iran (Islamic Republic of)| ir  
Iraq| iq  
Ireland| ie  
Israel| il  
Italy| it  
Jamaica| jm  
Japan| jp  
Jersey| je  
Jordan| jo  
Kazakhstan| kz  
Kenya| ke  
Kiribati| ki  
Korea (the Democratic People's Republic of)| kp  
Korea (the Republic of)| kr  
Kosovo| xk  
Kuwait| kw  
Kyrgyzstan| kg  
Lao People's Democratic Republic (the)| la  
Latvia| lv  
Lebanon| lb  
Lesotho| ls  
Liberia| lr  
Libya| ly  
Liechtenstein| li  
Lithuania| lt  
Luxembourg| lu  
Madagascar| mg  
Malawi| mw  
Malaysia| my  
Maldives| mv  
Mali| ml  
Malta| mt  
Marshall Islands (the)| mh  
Martinique| mq  
Mauritania| mr  
Mauritius| mu  
Mayotte| yt  
Mexico| mx  
Micronesia (Federated States of)| fm  
Moldova (the Republic of)| md  
Monaco| mc  
Mongolia| mn  
Montenegro| me  
Montserrat| ms  
Morocco| ma  
Mozambique| mz  
Myanmar| mm  
Namibia| na  
Nauru| nr  
Nepal| np  
Netherlands (the)| nl  
New Caledonia| nc  
New Zealand| nz  
Nicaragua| ni  
Niger (the)| ne  
Nigeria| ng  
Niue| nu  
Northern Cyprus| cy-2  
Norfolk Island| nf  
Northern Mariana Islands (the)| mp  
Norway| no  
Oman| om  
Pakistan| pk  
Palau| pw  
Palestine, State of| ps  
Panama| pa  
Papua New Guinea| pg  
Paraguay| py  
Peru| pe  
Philippines (the)| ph  
Pitcairn| pn  
Poland| pl  
Portugal| pt  
Pridnestrovian Moldavian Republic| pmr  
Puerto Rico| pr  
Qatar| qa  
Republic of North Macedonia| mk  
Romania| ro  
Russian Federation (the)| ru  
Rwanda| rw  
Réunion| re  
Saint Barthélemy| bl  
Saint Helena, Ascension and Tristan da Cunha| sh  
Saint Kitts and Nevis| kn  
Saint Lucia| lc  
Saint Martin (French part)| mf  
Saint Pierre and Miquelon| pm  
Saint Vincent and the Grenadines| vc  
Samoa| ws  
San Marino| sm  
Sao Tome and Principe| st  
Saudi Arabia| sa  
Senegal| sn  
Serbia| rs  
Seychelles| sc  
Sierra Leone| sl  
Singapore| sg  
Sint Maarten (Dutch part)| sx  
Slovakia| sk  
Slovenia| si  
Solomon Islands| sb  
Somalia| so  
Somaliland, Republic of| so-2  
South Africa| za  
South Georgia and the South Sandwich Islands| gs  
South Ossetia| so-3  
South Sudan| ss  
Spain| es  
Sri Lanka| lk  
Sudan (the)| sd  
Suriname| sr  
Svalbard and Jan Mayen| sj  
Sweden| se  
Switzerland| ch  
Syrian Arab Republic| sy  
Tajikistan| tj  
Tanzania, United Republic of| tz  
Thailand| th  
Timor-Leste| tl  
Togo| tg  
Tokelau| tk  
Tonga| to  
Trinidad and Tobago| tt  
Tunisia| tn  
Turkey| tr  
Turkmenistan| tm  
Turks and Caicos Islands (the)| tc  
Tuvalu| tv  
Uganda| ug  
Ukraine| ua  
United Arab Emirates (the)| ae  
United Kingdom of Great Britain and Northern Ireland (the)| gb  
United States Minor Outlying Islands (the)| um  
United States of America (the)| us  
Uruguay| uy  
Uzbekistan| uz  
Vanuatu| vu  
Venezuela (Bolivarian Republic of)| ve  
Viet Nam| vn  
Virgin Islands (British)| vg  
Virgin Islands (U.S.)| vi  
Wallis and Futuna| wf  
Western Sahara| eh  
Yemen| ye  
Zambia| zm  
Zimbabwe| zw  
Åland Islands| ax