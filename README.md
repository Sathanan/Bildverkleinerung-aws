# Bildverkleinerung-aws

Problem
: Das Verkleinern von Bildern ist umständlich

Lösung
: Unsere Lösung beeinhaltet zwei AWS S3 Buckets und eine Lambda Funktion, die Bilder von einem Bucket in den anderen schiebt und gleichzeitig verkleinert
<br>

#### 1. Buckets erstellen
Im ersten Schritt erstellen wir 2 Buckets &rarr; **imagedef** & **imagedef-resize**

imagedef
: enthält die unverarbeiteten Bilder

imagedef-resize
: enthält verarbeitete Bilder

#### 2. Lambda Funktion erstellen