'''

    El proposito de este script es crear los templates de los ads 
    y subirlo a servidor virtual.



   Requirements:
        imgkit -- Python 2 and 3 wrapper for wkhtmltoimage utility 
            to convert HTML to IMG using webkit. 
        jinja2 -- Templating engine that allows writing Python code in 
            inside HTML file.

    TODO: 
        -lista de backgrounds para los ads.
        -
        -run my code in the virtual server so it can run 24/7.
        
'''
import imgkit
from jinja2 import Environment
import random

#Lugar en el servidor donde voy a guardar la/s imagenes.
html_location = 'https://finsoftmarketing.fra1.digitaloceanspaces.com'

#lista de los bg templates de las imagenes.
quote_images = [r'C:\Users\cas\Documents\Automation\SM_Automation\images\banner0.jpeg',
                r'C:\Users\cas\Documents\Automation\SM_Automation\images\banner1.jpeg',
                r'C:\Users\cas\Documents\Automation\SM_Automation\images\banner2.jpeg',
                r'C:\Users\cas\Documents\Automation\SM_Automation\images\banner3.jpeg',
                r'C:\Users\cas\Documents\Automation\SM_Automation\images\banner4.jpeg'

] 

ad_images = [
    'https://finsoftmarketing.fra1.digitaloceanspaces.com/ram.jpeg',
    'https://finsoftmarketing.fra1.digitaloceanspaces.com/ram2.jpeg',
    'https://finsoftmarketing.fra1.digitaloceanspaces.com/ram3.jpeg',
]


#  
job_images = []

def createQuoteImg(msg_body, image_list, image_location):
    content = dict(
        backgroun_img_path = random.choice(image_list), #coge un template random de la lista de imagens
        description = msg_body, #descripcion del post de instagram
    )

    '''
        File de HTMl que 
    '''
    HTML = """
    <!DOCTYPE html> 
    <html>
    <head>
    <meta name="imgkit-format" content="jpeg"/>
    <meta name="imgkit-orientation" content="Landscape"/>
    
    <style tupe="text/css">

    @font-face {
    font-family: Monsterrat;
    src: url('path/to/font/source') #AñADIR EL SOURCE, TENGO QUE BAJARLO A MI MAQUINA.
    }
    
    .bottom-left{
      postition: absolute;
      bottom: 250px;
      left: 100px;
      width: 60%;
      font-size:50px;
      font-family:'Montserrat';
      line-height: 15&;
      color: #000;  
    }
    
    .top-right{
      postition: absolute;
      top: 60px;
      right: 60px;
      width: 100px;
    }
    
    </style>
    </head>

    <body>
    <div class="cointer">
        <img src="{{background_img_path}}" style="width:100%;">
        <div class="bottom-left"><p>{{description}}</p></div>   
    </div>
    </body>
    </html>
    """

    '''
        Crea objeto del env para poder usar html en python y
        guarda el template con los valores del dic content y
        con el script de HTML para crear el template final y
        que instagram lo pueda leer over http public server.
    
    '''
    render_output = Environment().from_string(HTML).render(**content)

    '''
        Abre un file donde estan los templates guarados, 
        añade el encoding utf8 para añadir simbolos, emojies, etc.
        f.write guarda el contenido de render output en html_location.

        Como IG solo recibe .jpeg hay que cambiarlo a .jpeg.

    '''
    with open(html_location, 'w', encoding='utf8') as f:
        f.write(render_output)


    options = {
        'xvfb': '',
        'encoding': 'UTF-8',
        "enable-local-file-access": None,
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
    }

    '''
        imgkit abre el file justamente creado en el html_location
        y lo exporta como un .jpeg file.

        image_location tiene que ser el virtual server.

    '''
    imgkit.from_file(html_location, image_location, options=options)


#Lugar en el servidor virtual donde se va a guardar la imagen para IG.
image_location = 'path/to/image'

#caption del post de IG.
msg_body = 'This is an automated post! :)'

createQuoteImg(msg_body, quote_images, image_location)

###########################-END-OF-CODE-########################################

