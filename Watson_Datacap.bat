echo off
title ---===IBM Watson For DataCap===---
cls

echo       ¦¦¦¦¦¦¦¦+¦ ¦¦+   ¦¦+¦ ¦¦¦¦¦+ ¦ ¦¦+   ¦¦¦+
echo        +--¦¦+--+ ¦¦¦¦+  ¦¦¦ ¦¦+--¦¦+ ¦¦¦¦+ ¦¦¦¦¦
echo           ¦¦¦    ¦¦+¦¦+ ¦¦¦ ¦¦¦¦¦¦++ ¦¦+¦¦¦¦+¦¦¦
echo           ¦¦¦    ¦¦¦+¦¦+¦¦¦ ¦¦+---+  ¦¦¦+¦¦++¦¦¦
echo           ¦¦¦    ¦¦¦ +¦¦¦¦¦ ¦¦¦      ¦¦¦ +-+ ¦¦¦
echo           +-+    +-+  +---+ +-+      +-+     +-+

    

timeout 2
cls
echo %time%
echo Loading IBM Watson For TNPM...
 
cd Watson_INPM\src\
..\..\Python\Python36\python.exe server.py
timeout 10
cls
echo %time%
echo Thank you for using IBM Watson For TNPM
timeout 2