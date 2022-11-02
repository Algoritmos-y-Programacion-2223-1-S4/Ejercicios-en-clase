from redactor import Redactor, JefeRedactor
from section import Seccion

def get_redactores_entretenimiento():
    return [
            Redactor("Leonardo",1234)
        ]
    """Redactor("Ana",1234),
        Redactor("Julia",1234),
        Redactor("Lorena ",1234),
        Redactor("Alan",1234),"""

def get_redactores_deportes():
    return [
            Redactor("Diego",1234),
        ]
    """Redactor("Fabrizio",1234),
        Redactor("Johana",1234),
        Redactor("Paula",1234),
        Redactor("Alfrdo",1234)"""

def get_redactores_farandula():
    return [
            Redactor("Mauricio",1234)
            ]
    """Redactor("Angel",1234),
        Redactor("Pedro",1234),
        Redactor("Maria",1234),
        Redactor("Jose",1234)"""

def process_articles(seccion):
    print("Inicio de labores en la seccion", seccion.nombre)
    articles = []
    for escritor in seccion.jefe_de_redactores.grupo_de_redactores:
        print("El escritor en labor es: ", escritor.nombre)
        articulo = escritor.escribir_articulo()
        print("El jefe al mando es: ", seccion.jefe_de_redactores.nombre)
        if seccion.jefe_de_redactores.decidir(articulo):
            articles.append(articulo)


def main():
    jefe_redactor_entretenimiento = JefeRedactor("Jose Quevedo",1234,get_redactores_entretenimiento())
    jefe_redactor_farandula = JefeRedactor("Luis Bello",1234,get_redactores_farandula())
    jefe_redactor_deporte = JefeRedactor("Antonio Guerra",1234,get_redactores_entretenimiento())

    seccion_entretenimiento = Seccion(jefe_redactor_entretenimiento, "Entretenimiento")
    seccion_farandula = Seccion(jefe_redactor_farandula, "Farandula")
    seccion_deportes = Seccion(jefe_redactor_deporte, "Deporte")
    article_list = []

    article_list += process_articles(seccion_entretenimiento)
    article_list += process_articles(seccion_farandula)
    article_list += process_articles(seccion_deportes)

main()