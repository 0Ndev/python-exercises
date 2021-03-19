Projekt Geometrische Figuren
Boris Grund FutureTrainings


1) Erstelle eine Klasse **Shape**

-	a) Shape besitzt zwei Member-Variablen **xOrgin** und **yOrgin** (Positon der Objekte) 
-	b) Beide Variablen sind vom Zugrifrecht her **protected/halbPrivat**
-	c) Die Methode **area()**, berechnet die Fläche
-	d) Die Methode **circumference()**, berechnet den Umfang
-	e) Die Methode **origin()**, gibt beide Positionen (xOrgin und yOrgin) 
                als einen String an den Aufruf zurück
-	f) Die Methode **toString()**, gibt an um welche Art von Form es sich handelt  


2) Erstelle eine Klasse **Circle**

-	a) Circle vererbt sich von der Klasse Shape
-	b) Die Klasse Circle besitzt folgende Member Variablen
	 	protected/halbPrivat (double) **radius** 
-	c) Umfang & Fläche Methoden als private und werden vom Konstruktor ausgelöst
  

3) Erstelle eine Klasse **Rectangle**

-	a) Rectangle vererbt sich ebenfalls von der Klasse Shape
-	b) Die Klasse Rectangle besitzt folgende Member Variablen
		protected/halbPrivat (int) **x**
 		protected/halbPrivat (int) **y**
-	c) Umfang & Fläche Methoden als private und werden vom Konstruktor ausgelöst


4) Erstelle eine Klasse **Square** 

-	a) Square vererbt sich von Rectangle und bekommt hat **x** als Wert
-	b) Umfang & Fläche Methoden als private und werden vom Konstruktor ausgelöst


5) Erstelle die Klasse **ShapeTester**, welche die main Methode besitzt
     und **alles Objektinstanzen generiert**


6) Ändere alle Zugriffsrechte der Member-Variablen von protected auf private
    und ändern sie die Klassen dahingehend das der Zugriff auf diese Variablen per **Getter und Setter Methoden** gehandelt wird  
