<h1> Análisis del discurso de los medios de prensa, Los Lagos</h1>
    <p>Se hará uso de la aplicación en desarrollo <a href="https://inf.uach.cl/investigacion/sophia-2/">Sophia2</a>,
    la cuál se encarga de monitorear medios de prensa chilenos, extrayendo el contenido de utilidad como su: <b>contenido, link de referencia, fecha de la noticia,
    medio de prensa.</b>.</p>
<h2>Objetivo del proyecto</h2>
    <p>El objetivo es <b>procesar</b> las noticias recolectadas, para ello se filtrarán las noticias <b>no vacías</b>, los textos serán también filtrados utilizando la librería <b>spacy</b> para palabras más importantes y achicar el contenido; y <b>gensim</b> para aplicar modelo <b>LDA</b> (Latent Dirichlet Allocation).</p>
    <h3>Ejemplo ficticio de uso:</h3>
        <h4><b>spacy</b></h4>
            <ul>
                <li>"Puerto Varas ha presentado un nuevo proyecto de áreas verdes" -> ["Puerto Varas","proyecto","áreas verdes"] ---- <b>Reduce el texto</b></li>
            </ul>
        <h4><b>gensim</b></h4>
            <ul>
                <li>["Puerto Varas","proyecto","áreas verdes"] -> [(0,1),(1,1),(2,1)] ---- <b>Transforma por id y cantidad</b> </li>
                <li>[(0,1),(1,1),(2,1)] -> LDA model ---- <b>Genera tópicos relacionados</b> </li>
                <li>LDA model -> ---- <b>Tópicos principales del texto </b> </li>
            </ul>
        <h4>transformers</h4>
            <ul>
                <li>"proyecto" -> POS ---- <b>Sentiment Analysis</b></li>
            </ul>
<h2>Enfoque</h2>
    <p>El enfoque del proyecto está dado para cumplir con alguna petición del Gobierno Regional de Los Lagos <b>(GORE)</b>, procesando las noticias de ciertos tópicos o palabras claves y generando un informe pdf.</p>
<h2>Algunas pistas de reflexiones para empezar…</h2>
    <h3>Elegir qué tipo de informe quieren producir: qué periodo de análisis, qué tema(s) de interés, cuál frecuencia del informe, qué indicadores pueden ayudar la toma de decisión del GORE…</b></h3>
        <p>---</p>
    <h3><b>Técnicas de TAL que conocen por el momento: Extracción de conceptos claves, Extracción de entidades, Análisis de tópicos, Word Embedding</b></h3>
        <p>Quizás la única que no se aplica directamente para análisis es Word Embedding</p>
    <h3><b>Representar los indicadores con visualización de datos (mapas de la región, gráfos, lineas de tiempo, etc.)</b></h3>
        <p>Se mostrarán mapas de la Región según tópicos de relevancia y positividad de las noticias</p>
    <h3><b>¿Qué ideas tienen para distinguir noticias "positivas" y noticias "negativas"?</b></h3>
        <p>Se aplicará <i>finiteautomata/beto-sentiment-analysis</i> para clasificar las noticias.</p>
