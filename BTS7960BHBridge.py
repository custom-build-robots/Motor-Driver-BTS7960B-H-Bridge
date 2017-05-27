#!/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Datum:   20160731
# Version:   2.0
# Homepage:   http://custom-build-robots.com

# Dieses Programm wurde fuer die Ansteuerung der linken und rechten
# Motoren des Roboter-Autos entwickelt. Es geht dabei davon aus,
# dass eine BTS7960B H-Bruecke als Motortreiber eingesetzt wird.

# Dieses Programm muss von einem uebergeordneten Programm aufgerufen 
# werden, dass die Steuerung des Programmes BTS7960BHBridge übernimmt.

# Es wird die Klasse RPi.GPIO importiert, die die Ansteuerung
# der GPIO Pins des Raspberry Pi ermoeglicht.
import RPi.GPIO as io
io.setmode(io.BCM)

# Die Variable PWM_MAX gibt die maximale Drehgeschwindigkeit der 
# Motoren als Prozentwert vor.
# Die Geschwindigkeit wird initial auf 70% der max Leistung der
# H-Bruecke gedrosselt um am Anfang mit der Steuerung des Roboter
# Autos besser zurecht zu kommen. Soll das Roboter-Auto schneller 
# fahren kann hier der Wert von 70% auf maximal 100% gesetzt werden.

PWM_MAX = 100

# Mit dem folgenden Aufruf werden eventuelle Warnungen die die 
# Klasse RPi.GPIO ausgibt deaktiviert.
io.setwarnings(False)

# Im folgenden Programmabschnitt wird die logische Verkabelung des 
# Raspberry Pi im Programm abgebildet. Dazu werden den vom Motor 
# Treiber bekannten Pins die GPIO Adressen zugewiesen.

# --- START KONFIGURATION GPIO Adressen ---

# Linker Motortreiber
L_L_EN = 22 # leftmotor_in1_pin
L_R_EN = 23 # leftmotor_in2_pin
L_L_PWM = 18 # leftmotorpwm_pin_l
L_R_PWM = 17 # leftmotorpwm_pin_r

# Rechter Motortreiber
R_L_EN = 13 # rightmotor_in1_pin
R_R_EN = 19 # rightmotor_in2_pin
R_L_PWM = 12 # rightmotorpwm_pin_l
R_R_PWM = 6 # rightmotorpwm_pin_r


# --- ENDE KONFIGURATION GPIO Adressen ---

# Der Variable leftmotor_in1_pin wird die Varibale IN1 zugeorndet. 
# Der Variable leftmotor_in2_pin wird die Varibale IN2 zugeorndet. 
leftmotor_in1_pin = L_L_EN
leftmotor_in2_pin = L_R_EN
# Beide Variablen leftmotor_in1_pin und leftmotor_in2_pin werden als
# Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehrichtung der Motoren gesteuert.
io.setup(leftmotor_in1_pin, io.OUT)
io.setup(leftmotor_in2_pin, io.OUT)

# Der Variable rightmotor_in1_pin wird die Varibale IN1 zugeorndet. 
# Der Variable rightmotor_in2_pin wird die Varibale IN2 zugeorndet. 
rightmotor_in1_pin = R_L_EN
rightmotor_in2_pin = R_R_EN
# Beide Variablen rightmotor_in1_pin und rightmotor_in2_pin werden 
# als Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehrichtung der Motoren gesteuert.
io.setup(rightmotor_in1_pin, io.OUT)
io.setup(rightmotor_in2_pin, io.OUT)

# Die GPIO Pins des Raspberry Pi werden initial auf False gesetzt.
# So ist sichger gestellt, dass kein HIGH Signal anliegt und der 
# Motor Treiber nicht unbeabsichtigt aktiviert wird.
io.output(leftmotor_in1_pin, True)
io.output(leftmotor_in2_pin, True)
io.output(rightmotor_in1_pin, True)
io.output(rightmotor_in2_pin, True)

# Der Variable leftmotorpwm_pin wird die Varibale ENA zugeorndet.
# Der Variable rightmotorpwm_pin wird die Varibale ENB zugeorndet.
leftmotorpwm_pin_l = L_L_PWM 
leftmotorpwm_pin_r = L_R_PWM

rightmotorpwm_pin_l = R_L_PWM
rightmotorpwm_pin_r = R_R_PWM

# Die Beide Variablen leftmotorpwm_pin und rightmotorpwm_pin werden 
# als Ausgaenge "OUT" definiert. Mit den beiden Variablen wird die
# Drehgeschwindigkeit der Motoren über ein PWM Signal gesteuert.
io.setup(leftmotorpwm_pin_l, io.OUT)
io.setup(leftmotorpwm_pin_r, io.OUT)

io.setup(rightmotorpwm_pin_l, io.OUT)
io.setup(rightmotorpwm_pin_r, io.OUT)

# Die Beide Variablen leftmotorpwm_pin und rightmotorpwm_pin werden 
# zusätzlich zu Ihrer Eigenschaft als Ausgaenge als "PWM" Ausgaenge
# definiert.
leftmotorpwm_l = io.PWM(leftmotorpwm_pin_l,100)
leftmotorpwm_r = io.PWM(leftmotorpwm_pin_r,100)

rightmotorpwm_l = io.PWM(rightmotorpwm_pin_l,100)
rightmotorpwm_r = io.PWM(rightmotorpwm_pin_r,100)

# Die linke Motoren steht still, da das PWM Signale mit 
# ChangeDutyCycle(0) auf 0 gesetzt wurde.
leftmotorpwm_l.start(0)
leftmotorpwm_r.start(0)

leftmotorpwm_l.ChangeDutyCycle(0)
leftmotorpwm_r.ChangeDutyCycle(0)

# Die rechten Motoren steht still, da das PWM Signale mit 
# ChangeDutyCycle(0) auf 0 gesetzt wurde.
rightmotorpwm_l.start(0)
rightmotorpwm_r.start(0)

rightmotorpwm_l.ChangeDutyCycle(0)
rightmotorpwm_r.ChangeDutyCycle(0)

# Die Funktion setMotorMode(motor, mode) legt die Drehrichtung der 
# Motoren fest. Die Funktion verfügt über zwei Eingabevariablen.
# motor      -> diese Variable legt fest ob der linke oder rechte 
#              Motor ausgewaehlt wird.
# mode      -> diese Variable legt fest welcher Modus gewaehlt ist
# Beispiel:
# setMotorMode(leftmotor, forward)   Der linke Motor ist gewaehlt
#                                   und dreht vorwaerts .
# setMotorMode(rightmotor, reverse)   Der rechte Motor ist ausgewaehlt 
#                                   und dreht rueckwaerts.
# setMotorMode(rightmotor, stopp)   Der rechte Motor ist ausgewaehlt
#                                   der gestoppt wird.

def setMotorMode(motor, mode):
   if motor == "leftmotor":
      if mode == "reverse":
         io.output(leftmotor_in1_pin, True)
         io.output(leftmotor_in2_pin, False)
      elif  mode == "forward":
         io.output(leftmotor_in1_pin, False)
         io.output(leftmotor_in2_pin, True)
      else:
         io.output(leftmotor_in1_pin, False)
         io.output(leftmotor_in2_pin, False)
   elif motor == "rightmotor":
      if mode == "reverse":
         io.output(rightmotor_in1_pin, False)
         io.output(rightmotor_in2_pin, True)      
      elif  mode == "forward":
         io.output(rightmotor_in1_pin, True)
         io.output(rightmotor_in2_pin, False)
      else:
         io.output(rightmotor_in1_pin, False)
         io.output(rightmotor_in2_pin, False)
   else:
      io.output(leftmotor_in1_pin, False)
      io.output(leftmotor_in2_pin, False)
      io.output(rightmotor_in1_pin, False)
      io.output(rightmotor_in2_pin, False)

# Die Funktion setMotorLeft(power) setzt die Geschwindigkeit der 
# linken Motoren. Die Geschwindigkeit wird als Wert zwischen -1
# und 1 uebergeben. Bei einem negativen Wert sollen sich die Motoren 
# rueckwaerts drehen ansonsten vorwaerts. 
# Anschliessend werden aus den uebergebenen Werten die notwendigen 
# %-Werte fuer das PWM Signal berechnet.

# Beispiel:
# Die Geschwindigkeit kann mit +1 (max) und -1 (min) gesetzt werden.
# Das Beispielt erklaert wie die Geschwindigkeit berechnet wird.
# SetMotorLeft(0)     -> der linke Motor dreht mit 0% ist gestoppt
# SetMotorLeft(0.75)  -> der linke Motor dreht mit 75% vorwaerts
# SetMotorLeft(-0.5)  -> der linke Motor dreht mit 50% rueckwaerts
# SetMotorLeft(1)     -> der linke Motor dreht mit 100% vorwaerts
def setMotorLeft(power):
   int(power)
   if power < 0:
      # Rueckwaertsmodus fuer den linken Motor
      #setMotorMode("leftmotor", "reverse")
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      leftmotorpwm_l.ChangeDutyCycle(pwm)
      leftmotorpwm_r.ChangeDutyCycle(0)	  
   elif power > 0:
      # Vorwaertsmodus fuer den linken Motor
      #setMotorMode("leftmotor", "forward")
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      leftmotorpwm_l.ChangeDutyCycle(0)
      leftmotorpwm_r.ChangeDutyCycle(pwm)
   else:
      # Stoppmodus fuer den linken Motor
      leftmotorpwm_l.ChangeDutyCycle(0)
      leftmotorpwm_r.ChangeDutyCycle(0)
	  
# Die Funktion setMotorRight(power) setzt die Geschwindigkeit der 
# rechten Motoren. Die Geschwindigkeit wird als Wert zwischen -1 
# und 1 uebergeben. Bei einem negativen Wert sollen sich die Motoren 
# rueckwaerts drehen ansonsten vorwaerts. 
# Anschliessend werden aus den uebergebenen Werten die notwendigen 
# %-Werte fuer das PWM Signal berechnet.

# Beispiel:
# Die Geschwindigkeit kann mit +1 (max) und -1 (min) gesetzt werden.
# Das Beispielt erklaert wie die Geschwindigkeit berechnet wird.
# setMotorRight(0)     -> der linke Motor dreht mit 0% ist gestoppt
# setMotorRight(0.75)  -> der linke Motor dreht mit 75% vorwaerts
# setMotorRight(-0.5)  -> der linke Motor dreht mit 50% rueckwaerts
# setMotorRight(1)     -> der linke Motor dreht mit 100% vorwaerts   
   
def setMotorRight(power):
   int(power)
   if power < 0:
      # Rueckwaertsmodus fuer den rechten Motor
      #setMotorMode("rightmotor", "reverse")
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      rightmotorpwm_l.ChangeDutyCycle(pwm)
      rightmotorpwm_r.ChangeDutyCycle(0)
   elif power > 0:
      # Vorwaertsmodus fuer den rechten Motor
      #setMotorMode("rightmotor", "forward")
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      rightmotorpwm_l.ChangeDutyCycle(0)
      rightmotorpwm_r.ChangeDutyCycle(pwm)
   else:
      # Stoppmodus fuer den rechten Motor
      rightmotorpwm_l.ChangeDutyCycle(0)
      rightmotorpwm_r.ChangeDutyCycle(0)
   
# Die Funktion exit() setzt die Ausgaenge die den Motor Treiber 
# steuern auf False. So befindet sich der Motor Treiber nach dem 
# Aufruf derFunktion in einem gesicherten Zustand und die Motoren 
# sind gestopped.
def exit():
   io.output(leftmotor_in1_pin, False)
   io.output(leftmotor_in2_pin, False)
   io.output(rightmotor_in1_pin, False)
   io.output(rightmotor_in2_pin, False)
   io.cleanup()
   
# Ende des Programmes
