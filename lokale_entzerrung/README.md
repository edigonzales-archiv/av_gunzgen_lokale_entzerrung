Messungen
---------
* Die Messungen wurden hauptsächlich mit den Testgeräten von Leica und Trimble durchgeführt.

Ausgleichung
------------
* Als Näherungskoordinaten werden die transformierten LV95-Koordinaten verwendet. Entsprechen den Soll-Koordinaten bei der Absteckung.
* Für die Näherungskoordinaten der GP-Höhen (und LFP3 ohne Höhe) werden die Höhen einer Messung verwendet.


gunzgen151201.txt (SLSE1)
-------------------------
* GNSS-Messungen für LTOP-Messfile werden aus dem Abschnitt "Messungen" verwendet.
* Einige Punktnummernverwechslungen. Das sieht man gut beim Abschnitt "Punktabsteckung" (2. Teil bei den Klammern). Das passte dann nicht mehr mit den "Messungen" resp. mit den Punktnummern im Messfile/Koofile/Steuerfile zusammen. -> Händisch flicken. 

gunzgen151201.txt (SLSE2)
-------------------------
* Einige Punkte, die in "gunzgen151201.txt" fehlen, sind hier doppelt aufgenommen (circa 30 Minuten Differenz). Mit Suffix "a". -> In die Session "gunzgen151201.txt" kopiert.
* `6005530` gelöscht. War dreifach (?) gemessen.
* zwei Punkte eliminiert (und in Session "gunzgen151201.txt")
  
GUNZGEN_TS3_151209.lqp (SLSE3)
------------------------------
* Ein paar Messungen gelöscht, da doppelt gemessen mit falscher Punktnummer.

GUNZGEN_TS3_151210.lqp (SLSE4)
------------------------------
* `6005522` gelöscht, da doppelt gemessen.
* `GS0002` gelöscht.

gunzgen151211_R8s.txt (SLSE5)
-----------------------------
* Einige Punkte in der Ausgleichung eliminiert. Scheinen die Punkte an der Gohlstrasse (Waldrand) zu sein.

2014-02-20 (SLSE6)
------------------
* ....

2014-02-27 (SLSE7)
------------------
* ....

2014-03-05 (SLSE8)
------------------
* Einige Doppelmessungen am gleichen Tag. Alle auf wenige Millimeter gleich. -> Eine Messung gelöscht.

2014-03-05 (SLSE8)
------------------
* `629544240349` doppelt in der gleichen Session. -> löschen.

2014-07-09 (SLSE9)
------------------
* `6005269` und `6005270` wieder gemessen. -> Eliminieren, aber prüfen wie gut die mit den anderen (eliminierten) übereinstimmen.
* `6005397`: eine Messung war auch bereits elimiert. -> zuerst mal alles eliminieren. (Raststätte, Waldrand)
* `6005271` nur in Session SE2 eliminiert -> Prüfen.

TODO
====

* Sind die Session genügend miteinander verknüpft?
* Die 2014er aus den Kontrollmessungen haben nie 4 TSP-Messungen, daher müssen sie über die Neupunkt genügend verknüpft sein.
* Was machen mit 1-fach-Messungen? Löschen.
* Herbie fertig messen lassen.
* Visuell überprüfen: Was ist bereits tiptop.
