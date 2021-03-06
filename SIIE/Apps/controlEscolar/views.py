# Django
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.contrib import messages
#Para imprimir en formatos
import csv
import xlwt
# Importa funcion para pdf que se encuentra en el archivo Utils.py
from Apps.controlEscolar.utils import render_to_pdf
#paginador
from django.core.paginator import Paginator
#Search Datos
from django.db.models import Q
#Models
from .models import (SeCatPais, SeCatUniversidad,SeCatNivelAcademico,SeCatPlaza,SeCatAreaBachillerato,
                    SeCatTipoBajas,SeCatMedioDifusion,SeCatBecas, SeCatTipoEscuela, SeCatTipoCambio,
                    SeCatIndicador, SeCatPlaEstudio, SeCatGrado)
#Views
from django.views.generic import View
#formularios
from .forms import (FormPaises, FormUniversidad, FormNivAca, FormPlaza, FormAreaBachi,FormTipoBajas,
                    FormMediosDifusion, FormTiposEscuelas,FormBecas,FormTipoCambio,FormPaises1,
                    FormsIndicador, FormsPlaE, FormsGrados)

# Create your views here.

##############################################   Paises   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaPaises(request):
    #Lista de todos los paises que tengan el status = A ordenados por id
    listaPaises = SeCatPais.objects.filter(estatus_pais="A").order_by('id_pais')
    contador_id = listaPaises.count() # Esta variable estara contando todos los registros de la consulta de arriba es decir tods los registros con status igual a "A"
    page = request.GET.get('page', 1) #Con esta variable inicializamos el paginador de indicamos que inidiara en la paguina 1 
    try: # En esta instruccion verificamos que la paguia que deseamos encontrar siempre exista y llenamos las paguinas del paginador con los registros de nuestra consulta anterior 
        paginator = Paginator(listaPaises, 7)
        listaPaises = paginator.page(page)
    except: # En caso de error harrojara un 404 de no encontrado
        raise Http404
    #Insercion de nuevos registros
    if request.method == 'POST': #Valida que sea una peticion de tipo post para poder Guarda datos
        form = FormPaises(request.POST) # Se inicializa el formulario
        if form.is_valid(): # Si el formulario es valido entra en el if
            form.save() # en este caso guarda todos los datos del formulario por que ingresamos el id pero en los fomularios que el id sea automatico cambia
            messages.success(request, "??Pais agregado con exito!") # Manda un mensaje al usuario desdes de que todos los datos son correctos, solo funciona con success(Verde), warning(Amarilla), info(Azul)      
            return redirect('vistaPaises') #redirecciona a la vista de nuevo
        else: # En caso de que alguno de los campos no sean correctos entra en el else y redirecciona al mismo formulario con los datos no correctos y por que no son correctos
            messages.warning(request, "??Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/GestionPaises.html",{'entity' : listaPaises,'paginator' : paginator,'FormPaises' : form,'contador': contador_id})       
    #Busqueda del search
    elif request.method == 'GET': #Valida que sea una peticion del form sea de tipo GET para poder realizar la busqueda de los datos
        busqueda = request.GET.get("search_paises", None) # En la variable guarda lo que se obtuvo de la barra de gusqueda
        if busqueda: # Si trae datos entra al if para poder hacer la consulta 
            listaPaises = SeCatPais.objects.filter( #Revisi??n de los campos de la tabla en la BD
                Q(descri_largo_pais__icontains = busqueda), # Busca el parametro de su preferencia 
                Q(estatus_pais__icontains = "A") # Y aparte valida que el estatus del registro cuente con status"A"
            ).distinct() #  Esto elimina las filas duplicadas de los resultados de la consulta
    form = FormPaises() # en la primera vuelta cuando entra a la vista no entra con una peticion post por lo que truena  y en necesario crear un formulario basio 
    data = { # Se crea un diccionario con los valores a emviar que son la consulta, el paginador, el formulario y el contador de registros
        'entity' : listaPaises,
        'paginator' : paginator,
        'FormPaises' : form,
        'contador': contador_id,
    }# Redirecciona a la vista principal 
    return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/GestionPaises.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarPais(request, id_pais):
    try:
        pais = SeCatPais.objects.get(id_pais=id_pais)
        pais.estatus_pais = "B"
    except SeCatPais.DoesNotExist:
        raise Http404("El pais no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Pais eliminado con exito!")
        pais.save()
        return redirect('vistaPaises')
    return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/BorrarPais.html", {"Pais": pais})
# Modifica un registro
def vista_paises_detail(request, pais_id):
    pais = SeCatPais.objects.get(id_pais=pais_id)
    form = FormPaises1(instance=pais)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormPaises1(request.POST, instance = pais)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "??Pais actualizado con exito!")
            return redirect('vistaPaises') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/ActualizarPais.html", {"pais": pais, "FormPaises" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/ActualizarPais.html", {"pais": pais, "FormPaises" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_paises(View):
    def get(self, request, *args, **kwargs):
        listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
        data = {
            'count': listaPaises.count(),
            'paises': listaPaises
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionPaises/listaPaises.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_paises(View):
    def get(self, request,*args, **kwargs):
        listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
        data = {
            'count': listaPaises.count(),
            'paises': listaPaises
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionPaises/listaPaises.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaPaises.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
def export_csv_paises (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaPaises.csv;'
    writer = csv.writer(response)
    writer.writerow(['id', 'Nombre', 'Abreviatura', 'Estatus'])
    listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for pais in listaPaises:
        writer.writerow([pais.id_pais, pais.descri_largo_pais, pais.descri_corto_pais, pais.estatus_pais])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
def export_xlwt_paises (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaPaises.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Paises')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['ID','Pais','Abreviacion','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatPais.objects.filter(estatus_pais="A").values_list('id_pais','descri_largo_pais','descri_corto_pais','estatus_pais')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
def listaPaises(request):
    #Lista de todos los paises
    listaPaises=SeCatPais.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/listaPaises.html", {"paises":listaPaises})

##############################################   Universidades   ##########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaUniversidades(request):
    #Lista de todas las universidades
    listaUniversidades=SeCatUniversidad.objects.filter(estatus_uni="A").order_by('id_uni')
    contador_id = listaUniversidades.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaUniversidades, 9)
        listaUniversidades = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormUniversidad(request.POST)
        if form.is_valid():
            uni = form.save(commit=False)
            ultimo_id = SeCatUniversidad.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            uni.id_uni = ultimo_id.id_uni + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??Universidad agregada con exito!")
            #redirecciona a la vista 
            return redirect('vistaUniversidades')
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/GestionUniversidades.html",{'entity' : listaUniversidades,'paginator' : paginator, 'FormUniversidad' : form,'contador' : contador_id,}) 
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_universidades", None)
        print(busqueda)
        if busqueda:
            listaUniversidades = SeCatUniversidad.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(nombre_uni__icontains = busqueda),
                Q(estatus_uni__icontains = "A") 
            ).distinct()
    form = FormUniversidad()
    data = {
        'entity' : listaUniversidades,
        'paginator' : paginator,
        'FormUniversidad' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/GestionUniversidades.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarUniversidad(request, id_uni):
    try:
        uni = SeCatUniversidad.objects.get(id_uni=id_uni)
        uni.estatus_uni = "B"
    except SeCatUniversidad.DoesNotExist:
        raise Http404("La Universidad no existe")
    
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "??Universidad eliminada con exito!")
        uni.save()
        return redirect('vistaUniversidades')
    return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/BorrarUniversidades.html", {"Universidad": uni})
# Modifica un registro
def vista_universidad_detail(request, uni_id):
    uni = SeCatUniversidad.objects.get(id_uni=uni_id)
    form = FormUniversidad(instance = uni)
    if request.POST: #Sobre escribe los valores
        form = FormUniversidad(request.POST, instance = uni)
        if form.is_valid():
            messages.info(request, "??Universidad actualizada con exito!")
            form.save()
            return redirect('vistaUniversidades') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/ActualizarUniversidad.html", {"uni": uni, "FormUniversidad" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/ActualizarUniversidad.html", {"uni": uni, "FormUniversidad" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir
class Export_print_universidades(View):
    def get(self, request, *args, **kwargs):
        listaUniversidades = SeCatUniversidad.objects.filter(estatus_uni="A") 
        data = {
            'count': listaUniversidades.count(),
            'uni': listaUniversidades
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionUniversidades/listaUniversidades.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Universidades
class Export_pdf_universidades(View):
    def get(self, request,*args, **kwargs):
        listaUniversidades=SeCatUniversidad.objects.filter(estatus_uni="A") 
        data = {
            'count': listaUniversidades.count(),
            'uni': listaUniversidades
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionUniversidades/listaUniversidades.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaUniversidades.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar universidades a CSV sin libreria 
def export_csv_universidades (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaUniversidades.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Universidad', 'Organizacion', 'Direccion', 'RFC', 'Estado', 'Delegacion',
                    'Colonia', 'Pais', 'Codigo Postal', 'Tel 1', 'Tel 2', 'Tel 3', 'Fax 1', 'Fax 2',
                    'Fax 3', 'Ext 1', 'Ext 2', 'Ext 3', 'Email', 'Pag. Internet', 'Contacto', 'Estatus'])
    listaUniversidades=SeCatUniversidad.objects.filter(estatus_uni="A") 
    for uni in listaUniversidades:
        writer.writerow([uni.id_uni, uni.nombre_uni, uni.tipo_org_uni, uni.direccion_uni, uni.rfc_uni,
                        uni.estado_uni, uni.delmun_uni, uni.colonia_uni, uni.pais_uni,uni.codpos_uni, uni.telefono1_uni,
                        uni.telefono2_uni, uni.telefono3_uni, uni.fax1_uni, uni.fax2_uni, uni.fax3_uni,
                        uni.ext1_uni, uni.ext2_uni, uni.ext3_uni, uni.mail_uni, uni.pagina_internet_uni, uni.contacto_uni, uni.estatus_uni])
    return response
# Exportar universidades a xlwt sin con la libreria XLWT 
def export_xlwt_universidades (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaUniversidades.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Universidades')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Universidad', 'Organizacion', 'Direccion', 'RFC', 'Estado', 'Delegacion',
                'Colonia', 'Pais', 'Codigo Postal', 'Tel 1', 'Tel 2', 'Tel 3', 'Fax 1', 'Fax 2',
                'Fax 3', 'Ext 1', 'Ext 2', 'Ext 3', 'Email', 'Pag. Internet', 'Contacto', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatUniversidad.objects.filter(estatus_uni="A").values_list('id_uni','nombre_uni','tipo_org_uni','direccion_uni', 'rfc_uni',
                                                                    'estado_uni', 'delmun_uni', 'colonia_uni', 'pais_uni','codpos_uni', 'telefono1_uni',
                                                                    'telefono2_uni', 'telefono3_uni', 'fax1_uni', 'fax2_uni', 'fax3_uni',
                                                                    'ext1_uni', 'ext2_uni', 'ext3_uni', 'mail_uni', 'pagina_internet_uni', 'contacto_uni', 'estatus_uni')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################  Nivel Academico  ##########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaNivelAca(request):
    #Lista de todas las divisiones
    listaNivelAca = SeCatNivelAcademico.objects.filter(estatus_acade="A").order_by('id_academico')
    contador_id = listaNivelAca.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaNivelAca, 9)
        listaNivelAca = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormNivAca(request.POST)
        if form.is_valid():
            aca = form.save(commit=False)
            ultimo_id = SeCatNivelAcademico.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            aca.id_academico = ultimo_id.id_academico + 1 # agrega uno al ultimo id insertado
            form.save() # Guadar lo ingresadoa l formulario
            messages.success(request, "??Nivel Academico agregada con exito!")
            return redirect('vistaNivelAca') #redirecciona a la vista 
        else :
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/GestionNivelAcademico.html",{'entity' : listaNivelAca,'paginator' : paginator,'FormNivAca' : form,'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_nivelaca", None)
        print(busqueda)
        if busqueda:
            listaNivelAca = SeCatNivelAcademico.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_largo_acade__icontains = busqueda),
                Q(estatus_acade__icontains = "A")
            ).distinct()
    form = FormNivAca()
    data = {
        'entity' : listaNivelAca,
        'paginator' : paginator,
        'FormNivAca' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/GestionNivelAcademico.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarNivelAca(request, id_academico):
    try:
        aca = SeCatNivelAcademico.objects.get(id_academico=id_academico)
        aca.estatus_acade = "B"
    except SeCatNivelAcademico.DoesNotExist:
        raise Http404("El nivel academico no existe")
    
    if request.POST: #Sobre escribe los valores
        messages.warning(request, "??Nivel academico eliminado con exito!")
        aca.save()
        return redirect('vistaNivelAca')
    return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/BorrarNivelAcademico.html", {"Academico": aca})
# Modifica un registro
def vista_nivel_aca_detail(request, aca_id):
    aca = SeCatNivelAcademico.objects.get(id_academico=aca_id)
    form = FormNivAca(instance = aca)
    if request.POST: #Sobre escribe los valores
        form = FormNivAca(request.POST, instance = aca)
        if form.is_valid():
            messages.info(request, "??Nivel academico actualizado con exito!")
            form.save()
            return redirect('vistaNivelAca') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/ActualizarNivelAcademico.html", {"aca": aca, "FormNivAca" : form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/ActualizarNivelAcademico.html", {"aca": aca, "FormNivAca" : form})#envia al detalle para actualizar
#Imprimir pfd
class Export_print_nivel_academico(View):
    def get(self, request, *args, **kwargs):
        listaNivelAca = SeCatNivelAcademico.objects.filter(estatus_acade="A") 
        data = {
            'count': listaNivelAca.count(),
            'aca': listaNivelAca
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionNivelAcademico/ListaNivelAcademico.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_nivel_academico(View):
    def get(self, request,*args, **kwargs):
        listaNivelAca=SeCatNivelAcademico.objects.filter(estatus_acade="A") 
        data = {
            'count': listaNivelAca.count(),
            'aca': listaNivelAca
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionNivelAcademico/ListaNivelAcademico.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaNivelAcademico.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria 
def export_csv_nivel_academico (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaNivelAcademico.csv;'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Descripcion', 'Abreviatura', 'Estatus'])
    listaNivelAca=SeCatNivelAcademico.objects.filter(estatus_acade="A") 
    for aca in listaNivelAca:
        writer.writerow([aca.id_academico, aca.descri_largo_acade, aca.descri_corto_acade, aca.estatus_acade])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT 
def export_xlwt_nivel_academico (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaNivelAcademico.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Nivel Academico')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['ID', 'Descripcion', 'Abreviatura', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatNivelAcademico.objects.filter(estatus_acade="A").values_list('id_academico', 'descri_largo_acade',
                                                                    'descri_corto_acade', 'estatus_acade')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################  Plaza  ##########################################################
#Agregar si es post y lista de todos / Aqui va la paginaci??n
def vistaPlaza(request):
    #Lista de todas las divisiones
    listaPlaza = SeCatPlaza.objects.filter(estatus_plaza="A").order_by('id_plaza')
    contador_id = listaPlaza.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaPlaza, 9)
        listaPlaza = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormPlaza(request.POST)
        if form.is_valid():
            plaza = form.save(commit=False)
            ultimo_id = SeCatPlaza.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            plaza.id_plaza = ultimo_id.id_plaza + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??Plaza agregada con exito!") 
            return redirect('vistaPlaza') #redirecciona a la vista
        else :
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/GestionPlazas.html",{'entity' : listaPlaza, 'paginator' : paginator, 'FormPlaza' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_plaza", None)
        if busqueda:
            listaPlaza = SeCatPlaza.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_largo_plaza__icontains = busqueda),
                Q(estatus_plaza__icontains = "A")
            ).distinct()
    form = FormPlaza()
    data = {
        'entity' : listaPlaza,
        'paginator' : paginator,
        'FormPlaza' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/GestionPlazas.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarPlaza(request, id_plaza):
    try:
        pla = SeCatPlaza.objects.get(id_plaza=id_plaza)
        #aca.estatus_acade = "B"
    except SeCatPlaza.DoesNotExist:
        raise Http404("La plaza no existe")
    
    if request.POST: #Sobre escribe los valores
        messages.warning(request, "??Plaza eliminada con exito!")
        pla.save()
        return redirect('vistaPlaza')
    return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/BorrarPlazas.html", {"Plazas": pla})
# Modifica un registro
def vista_plaza_detail(request, plaza_id):
    pla = SeCatPlaza.objects.get(id_plaza=plaza_id)
    form = FormPlaza(instance = pla)
    if request.POST: #Sobre escribe los valores
        form = FormPlaza(request.POST, instance = pla)
        if form.is_valid():
            messages.info(request, "??Plaza actualizada con exito!")
            form.save()
        return redirect('vistaPlaza') #retorna despues de actualizar
    return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/ActualizarPlazas.html", {"pla": pla, "FormPlaza" : form})#envia al detalle para actualizar
# imprime 
class Export_print_plaza(View):
    def get(self, request, *args, **kwargs):
        listaPlaza = SeCatPlaza.objects.filter(estatus_plaza="A") 
        data = {
            'count': listaPlaza.count(),
            'pla': listaPlaza
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionPlazas/listaPlazas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_plaza(View):
    def get(self, request,*args, **kwargs):
        listaPlaza=SeCatPlaza.objects.filter(estatus_plaza="A") 
        data = {
            'count': listaPlaza.count(),
            'pla': listaPlaza
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionPlazas/listaPlazas.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaPlazas.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria 
def export_csv_plaza (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaPlazas.csv;'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Plaza', 'Abreviatura', 'Estatus'])
    listaPlaza=SeCatPlaza.objects.filter(estatus_plaza="A") 
    for pla in listaPlaza:
        writer.writerow([pla.id_plaza, pla.descri_largo_plaza, pla.descri_corto_plaza, pla.estatus_plaza])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT 
def export_xlwt_plaza (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaPlazas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Nivel Academico')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['ID', 'Plazas', 'Abreviatura', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatPlaza.objects.filter(estatus_plaza="A").values_list('id_plaza', 'descri_largo_plaza',
                                                                    'descri_corto_plaza', 'estatus_plaza')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################  Areas Bachillerato  ######################################################
#Agregar si es post y lista de todos / Aqui va la paginaci??n
def vistaAreaBachi(request):
    #Lista todas las areas del bachillerato que tengan el status = A
    listaAreaBachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A").order_by('id_area_bac')
    contador_id = listaAreaBachi.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaAreaBachi, 9)
        listaAreaBachi = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormAreaBachi(request.POST)
        if form.is_valid():
            areabachillerato=form.save(commit=False)
            ultimo_id=SeCatAreaBachillerato.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            areabachillerato.id_area_bac=ultimo_id.id_area_bac + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??Area bachillerato fue agregado con exito!")         
            return redirect('vistaAreaBachi')#redirecciona a la vista    
        else :
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/GestionAreaBachi/GestionAreaBachi.html",{'entity' : listaAreaBachi, 'paginator' : paginator, 'FormAreaBachi' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_areabachillerato", None)
        if busqueda:
            listaAreaBachi = SeCatAreaBachillerato.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_larga_bac__icontains = busqueda) 
            ).distinct()
    form = FormAreaBachi()
    data = {
        'entity' : listaAreaBachi,
        'paginator' : paginator,
        'FormAreaBachi' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/GestionAreaBachi/GestionAreaBachi.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarAreaBachi(request, id_area_bac):
    try:
        areabachi = SeCatAreaBachillerato.objects.get(id_area_bac=id_area_bac)
        areabachi.estatus_bac = "B"
    except SeCatAreaBachillerato.DoesNotExist:
        raise Http404("El area bachillerato no existe")
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "??El area  bachillerato fue  eliminada con exito!")
        areabachi.save()
        return redirect('vistaAreaBachi')
    return render(request, "controlEscolar/catalogos/estudiantes/GestionAreaBachi/BorrarAreaBachi.html", {"AreaBachi":areabachi})
# Modifica un registro
def vista_Area_Bac_detail(request, id_area_bac):
    areabachi= SeCatAreaBachillerato.objects.get(id_area_bac=id_area_bac)
    form = FormAreaBachi(instance=areabachi)
    if request.POST: #Sobre escrive los valores
        form = FormAreaBachi(request.POST, instance = areabachi)
        if form.is_valid():
            messages.info(request, "??El Area de Bachillerato fue actualizado con exito!")
            #redirecciona a la vista 
            form.save()
            return redirect('vistaAreaBachi') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/estudiantes/GestionAreaBachi/ActualizarAreaBachi.html", {"AreaBachi": areabachi, "FormAreaBachi" : form})#envia al detalle con los errores
    return render(request, "controlEscolar/catalogos/estudiantes/GestionAreaBachi/ActualizarAreaBachi.html", {"AreaBachi": areabachi, "FormAreaBachi" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_area_bac(View):
    def get(self, request, *args, **kwargs):
        areabachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A") 
        data = {
            'count': areabachi.count(),
            'areabachi': areabachi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/GestionAreaBachi/ListaAreaBachi.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_area_bachi(View):
    def get(self, request,*args, **kwargs):
        areabachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A") 
        data = {
            'count': areabachi.count(),
            'areabachi': areabachi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/GestionAreaBachi/ListaAreaBachi.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaAreaBachillerato.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
def export_csv_area_bachi (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaAreaBachillerato.csv;'
    writer = csv.writer(response)
    writer.writerow(['id', 'Nombre', 'Abreviatura', 'Estatus'])
    areabachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for areabac in areabachi:
        writer.writerow([areabac.id_area_bac, areabac.descri_larga_bac, areabac.descri_corta_bac, areabac.estatus_bac])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
def export_xlwt_areabachi (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaAreaBachillerato.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Area Bac')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['ID','Nombre','Abreviacion','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatAreaBachillerato.objects.filter(estatus_bac="A").values_list('id_area_bac','descri_larga_bac','descri_corta_bac','estatus_bac')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################  Tipos de Baja ######################################################
#Agregar si es post y lista de todos / Aqui va la paginaci??n
def vistaTipoBajas(request):
    #Lista de todos los paises que tengan el status = A
    listaTipoBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A").order_by('id_tipo_baj')
    contador_id = listaTipoBajas.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaTipoBajas, 9)
        listaTipoBajas = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormTipoBajas(request.POST)
        if form.is_valid():
            tipobaja=form.save(commit=False)
            ultimo_id = SeCatTipoBajas.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            tipobaja.id_tipo_baj = ultimo_id.id_tipo_baj + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??Tipo de Baja agregado con exito!")         
            return redirect('vistaTipoBajas') #redirecciona a la vista   
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/GestionTipoBajas/GestionTipoBajas.html",{'entity' : listaTipoBajas,'paginator' : paginator,'FormTipoBajas' : form,'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_tipobajas", None)
        if busqueda:
            listaTipoBajas = SeCatTipoBajas.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_largo_tipo_baj__icontains = busqueda) 
            ).distinct()
    form = FormTipoBajas()
    data = {
        'entity' : listaTipoBajas,
        'paginator' : paginator,
        'FormTipoBajas' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/GestionTipoBajas/GestionTipoBajas.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarTipoBajas(request, id_tipo_baj):
    try:
        tipobajas = SeCatTipoBajas.objects.get(id_tipo_baj=id_tipo_baj)
        tipobajas.estatus_tipo_baj = "B"
    except SeCatTipoBajas.DoesNotExist:
        raise Http404("El tipo de baja no existe")
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "??Tipo de Baja eliminado con exito!")
        tipobajas.save()
        return redirect('vistaTipoBajas')
    return render(request, "controlEscolar/catalogos/estudiantes/GestionTipoBajas/BorrarTipoBajas.html", {"TipoBaja":tipobajas})
# Modifica un registro
def vista_tipobajas_detail(request, id_tipo_baj):
    tipobajas = SeCatTipoBajas.objects.get(id_tipo_baj=id_tipo_baj)
    form = FormTipoBajas(instance=tipobajas)
    if request.POST: #Sobre escrive los valores
        form = FormTipoBajas(request.POST, instance = tipobajas)
        if form.is_valid():
            messages.info(request, "??Tipo de Baja actualizado con exito!")
            #redirecciona a la vista 
            form.save()
            return redirect('vistaTipoBajas') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/estudiantes/GestionTipoBajas/ActualizarTipoBajas.html", {"TipoBaja":tipobajas , "FormTipoBajas" : form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/estudiantes/GestionTipoBajas/ActualizarTipoBajas.html", {"TipoBaja":tipobajas , "FormTipoBajas" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_tipobajas(View):
    def get(self, request, *args, **kwargs):
        listaTipoBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A") 
        data = {
            'count': listaTipoBajas.count(),
            'tipobajas': listaTipoBajas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/GestionTipoBajas/listaTipoBajas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_tipo_bajas(View):
    def get(self, request,*args, **kwargs):
        listaTipoBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A") 
        data = {
            'count': listaTipoBajas.count(),
            'tipobajas': listaTipoBajas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/GestionTipoBajas/listaTipoBajas.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaTipoBajas.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar tipo de bajas a CSV sin libreria 
def export_csv_tipo_bajas (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaTipoBajas.csv;'
    writer = csv.writer(response)
    writer.writerow(['id', 'Nombre', 'Abreviatura', 'Estatus'])
    listaTipoBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A") 
    # listaTipoBajas=SeCatTipoBajas.objects.filter(owner=request.user)
    for tipobajas in listaTipoBajas:
        writer.writerow([tipobajas.id_tipo_baj, tipobajas.descri_largo_tipo_baj, tipobajas.descri_corto_tipo_baj, tipobajas.estatus_tipo_baj])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
def export_xlwt_tipo_bajas (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaTipoBajas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tipos Bajas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['ID','Nombre','Abreviacion','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A").values_list('id_tipo_baj','descri_largo_tipo_baj','descri_corto_tipo_baj','estatus_tipo_baj')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################   Medios de difusi??n  ########################################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaMedios(request):
    #Lista de todos los paises que tengan el status = A
    listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A").order_by('id_medio_dif')
    contador_id = listaMedios.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaMedios, 9)
        listaMedios = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormMediosDifusion(request.POST)
        if form.is_valid():
            medio = form.save(commit=False)
            ultimo_id = SeCatMedioDifusion.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            medio.id_medio_dif = ultimo_id.id_medio_dif + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??Medio de Difusi??n agregado con exito!")
            return redirect('vistaMedios')#redirecciona a la vista 
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/GestionMD.html",{'entity' : listaMedios, 'paginator' : paginator, 'FormMediosDifusion' : form, 'contador': contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_medios", None)
        print(busqueda)
        if busqueda:
            listaMedios = SeCatMedioDifusion.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_largo_meddif__icontains = busqueda),
                Q(estatus_dif__icontains = "A")
            ).distinct()
    form = FormMediosDifusion()
    data = {
        'entity' : listaMedios,
        'paginator' : paginator,
        'FormMediosDifusion' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/GestionMD.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarMedio(request, id_medio_dif):
    try:
        medio = SeCatMedioDifusion.objects.get(id_medio_dif=id_medio_dif)
        medio.estatus_dif = "B"
    except SeCatMedioDifusion.DoesNotExist:
        raise Http404("El Medio de Difusi??n no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Medio de Difusi??n eliminado con exito!")
        medio.save()
        return redirect('vistaMedios')
    return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/BorrarMD.html", {"Medio": medio})
# Modifica un registro
def vista_medios_detail(request, medio_id):
    medio = SeCatMedioDifusion.objects.get(id_medio_dif=medio_id)
    form = FormMediosDifusion(instance=medio)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormMediosDifusion(request.POST, instance = medio)
        if form.is_valid():
            medio.save() #Guarda cambios
            messages.info(request, "??Medio de Difusi??n actualizado con exito!")
            form.save()
            return redirect('vistaMedios') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/ActualizarMD.html", {"medio": medio, "FormMediosDifusion" : form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/ActualizarMD.html", {"medio": medio, "FormMediosDifusion" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_medios(View):
    def get(self, request, *args, **kwargs):
        listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A") 
        data = {
            'count': listaMedios.count(),
            'medios': listaMedios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionMediosDifusion/listaMD.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_medios(View):
    def get(self, request,*args, **kwargs):
        listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A") 
        data = {
            'count': listaMedios.count(),
            'medios': listaMedios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionMediosDifusion/listaMD.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaMediosDifusion.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
def export_csv_medios (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaMediosDifusion.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id Medio de Difusion', 'Medio de Difusion', 'Abreviatura', 'Estatus'])
    listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for medio in listaMedios:
        writer.writerow([medio.id_medio_dif, medio.descri_largo_meddif, medio.descri_corto_meddif, medio.estatus_dif])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
def export_xlwt_medios (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaMediosDifusion.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Medios')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id Medio Difusion', 'Medio Difusion', 'Abreviatura', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatMedioDifusion.objects.filter(estatus_dif="A").values_list('id_medio_dif','descri_largo_meddif','descri_corto_meddif', 'estatus_dif')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
def listaMedios(request):
    #Lista de todos los paises
    listaMedios=SeCatMedioDifusion.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/listaMD.html", {"medios":listaMedios})

###################################################   Tipo de Escuelas  ########################################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaEscuelas(request):
    #Lista de todos los paises que tengan el status = A
    listaEscuelas=SeCatTipoEscuela.objects.filter(estatus_esc="A").order_by('id_tipo_esc')
    contador_id = listaEscuelas.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaEscuelas, 4)
        listaEscuelas = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormTiposEscuelas(request.POST)
        if form.is_valid():
            escuela = form.save(commit=False)
            ultimo_id = SeCatTipoEscuela.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            escuela.id_tipo_esc = ultimo_id.id_tipo_esc + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??Escuela agregada con exito!")
            return redirect('vistaEscuelas')#redirecciona a la vista 
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/GestionEscuelas.html",{'entity' : listaEscuelas, 'paginator' : paginator, 'FormTiposEscuelas' : form, 'contador': contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_escuelas", None)
        print(busqueda)
        if busqueda:
            listaEscuelas = SeCatTipoEscuela.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_largo_esc__icontains = busqueda),
                Q(estatus_esc__icontains = "A")
            ).distinct()
    form = FormTiposEscuelas()
    data = {
        'entity' : listaEscuelas,
        'paginator' : paginator,
        'FormTiposEscuelas' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/GestionEscuelas.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarEscuela(request, id_tipo_esc):
    try:
        escuela = SeCatTipoEscuela.objects.get(id_tipo_esc=id_tipo_esc)
        escuela.estatus_esc = "B"
    except SeCatTipoEscuela.DoesNotExist:
        raise Http404("La Escuela no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Escuela eliminada con exito!")
        escuela.save()
        return redirect('vistaEscuelas')
    return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/BorrarEscuela.html", {"Escuela": escuela})
# Modifica un registro
def vista_escuelas_detail(request, escuela_id):
    escuela = SeCatTipoEscuela.objects.get(id_tipo_esc=escuela_id)
    form = FormTiposEscuelas(instance=escuela)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormTiposEscuelas(request.POST, instance = escuela)
        if form.is_valid():
            escuela.save() #Guarda cambios
            messages.info(request, "??Escuela actualizada con exito!")
            form.save()
            return redirect('vistaEscuelas') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/ActualizarEscuela.html", {"escuela": escuela, "FormTiposEscuelas" : form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/ActualizarEscuela.html", {"escuela": escuela, "FormTiposEscuelas" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_escuelas(View):
    def get(self, request, *args, **kwargs):
        listaEscuelas=SeCatTipoEscuela.objects.filter(estatus_esc="A") 
        data = {
            'count': listaEscuelas.count(),
            'escuelas': listaEscuelas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/listaEscuelas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_escuelas(View):
    def get(self, request,*args, **kwargs):
        listaEscuelas=SeCatTipoEscuela.objects.filter(estatus_esc="A") 
        data = {
            'count': listaEscuelas.count(),
            'escuelas': listaEscuelas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/listaEscuelas.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaTiposdeEscuelas.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
def export_csv_escuelas (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposdeEscuelas.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Tipo de Escuela', 'Abreviatura', 'Clave Estado','Clave Municipio/Delegaci??n','Nombre Instituci??n','Nombre Plantel','Estatus'])
    listaEscuelas=SeCatTipoEscuela.objects.filter(estatus_esc="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for esc in listaEscuelas:
        writer.writerow([esc.id_tipo_esc, esc.descri_largo_esc, esc.descri_corta_esc, esc.id_edo, esc.id_mundel, esc.institucion, esc.nombre_plantel, esc.estatus_esc])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
def export_xlwt_escuelas (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposEscuelas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Escuelas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Tipo de Escuela', 'Abreviatura', 'Clave Estado','Clave Municipio/Delegaci??n','Nombre Instituci??n','Nombre Plantel','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatTipoEscuela.objects.filter(estatus_esc="A").values_list('id_tipo_esc','descri_largo_esc','descri_corta_esc', 'id_edo', 'id_mundel', 'institucion', 'nombre_plantel', 'estatus_esc')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
def listaEscuelas(request):
    #Lista de todos los paises
    listaEscuelas=SeCatTipoEscuela.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/listaEscuelas.html", {"escuelas":listaEscuelas})

###################################################   Becas  ########################################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaBecas(request):
    #Lista de todos los paises que tengan el status = A
    listaBecas=SeCatBecas.objects.filter(estatus_bec="A").order_by('id_becas')
    contador_id = listaBecas.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaBecas, 9)
        listaBecas = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormBecas(request.POST)
        if form.is_valid():
            beca = form.save(commit=False)
            ultimo_id = SeCatBecas.objects.all().last()
            beca.id_becas = ultimo_id.id_becas + 1
            form.save()
            messages.success(request, "??Beca agregada con exito!")
            return redirect('vistaBecas')#redirecciona a la vista 
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Becas/GestionBecas.html",{'entity' : listaBecas,'paginator' : paginator,'FormBecas' : form,'contador' : contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_becas", None)
        print(busqueda)
        if busqueda:
            listaBecas = SeCatBecas.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(id_becas__icontains = busqueda),
                Q(estatus_bec__icontains = "A") 
            ).distinct()
    form = FormBecas()
    data = {
        'entity' : listaBecas,
        'paginator' : paginator,
        'FormBecas' : form,
        'contador' : contador_id
    }
    return render(request, "controlEscolar/catalogos/estudiantes/Becas/GestionBecas.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarBeca(request, id_becas):
    try:
        beca = SeCatBecas.objects.get(id_becas=id_becas)
        beca.estatus_bec = "B"
    except SeCatBecas.DoesNotExist:
        raise Http404("La Beca no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Beca eliminada con exito!")
        beca.save()
        return redirect('vistaBecas')
    return render(request, "controlEscolar/catalogos/estudiantes/Becas/BorrarBeca.html", {"Beca": beca})
# Modifica un registro
def vista_becas_detail(request, beca_id):
    beca = SeCatBecas.objects.get(id_becas=beca_id)
    form = FormBecas(instance=beca)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormBecas(request.POST, instance = beca)
        if form.is_valid():
            beca.save() #Guarda cambios
            messages.info(request, "??Beca actualizada con exito!")
            form.save()
            return redirect('vistaBecas') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/estudiantes/Becas/ActualizarBeca.html", {"beca": beca, "FormBecas" : form}) #envia al detalle de errores
    return render(request, "controlEscolar/catalogos/estudiantes/Becas/ActualizarBeca.html", {"beca": beca, "FormBecas" : form}) #envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_becas(View):
    def get(self, request, *args, **kwargs):
        listaBecas=SeCatBecas.objects.filter(estatus_bec="A") 
        data = {
            'count': listaBecas.count(),
            'becas': listaBecas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Becas/listaBecas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_becas(View):
    def get(self, request,*args, **kwargs):
        listaBecas=SeCatBecas.objects.filter(estatus_bec="A") 
        data = {
            'count': listaBecas.count(),
            'becas': listaBecas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Becas/listaBecas.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaBecas.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
def export_csv_becas (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaBecas.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Valor Inicial', 'Valor Final', 'Porcentaje', 'Estatus'])
    listaBecas=SeCatBecas.objects.filter(estatus_bec="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for bs in listaBecas:
        writer.writerow([bs.id_becas, bs.valor_ini_bec, bs.valor_fin_bec, bs.porcentaje_beca, bs.estatus_bec])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
def export_xlwt_becas (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaBecas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Becas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Valor Inicial', 'Valor Final', 'Porcentaje', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatBecas.objects.filter(estatus_bec="A").values_list('id_becas','valor_ini_bec','valor_fin_bec', 'porcentaje_beca', 'estatus_bec')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
def listaBecas(request):
    #Lista de todos los paises
    listaBecas=SeCatBecas.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/estudiantes/Becas/listaBecas.html", {"becas":listaBecas})
###################################################   Tipo Cambio  ########################################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaCambios(request):
    #Lista de todos los paises que tengan el status = A
    listaCambios=SeCatTipoCambio.objects.filter(status="A").order_by('id_tipo_cambio')
    contador_id = listaCambios.count() 
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaCambios, 9)
        listaCambios = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormTipoCambio(request.POST)
        if form.is_valid():
            cambio = form.save(commit=False)
            ultimo_id = SeCatTipoCambio.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            cambio.id_tipo_cambio = ultimo_id.id_tipo_cambio + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??Tipo de Cambio agregaoa con exito!") 
            return redirect('vistaCambios')#redirecciona a la vista
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/GestionTipoCambios.html",{'entity' : listaCambios,'paginator' : paginator,'FormTipoCambio' : form,'contador': contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_cambios", None)
        print(busqueda)
        if busqueda:
            listaCambios = SeCatTipoCambio.objects.filter( #Revisi??n de los campos de la tabla en la BD
                Q(descri_tipocambio__icontains = busqueda),
                Q(status__icontains = "A")
            ).distinct()
    form = FormTipoCambio()
    data = {
        'entity' : listaCambios,
        'paginator' : paginator,
        'FormTipoCambio' : form,
        'contador': contador_id,      
    }
    return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/GestionTipoCambios.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
def eliminarCambio(request, id_tipo_cambio):
    try:
        cambio = SeCatTipoCambio.objects.get(id_tipo_cambio=id_tipo_cambio)
        cambio.status = "B"
    except SeCatTipoCambio.DoesNotExist:
        raise Http404("El Tipo de Cambio no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Tipo de Cambio eliminado con exito!")
        cambio.save()
        return redirect('vistaCambios')
    return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/BorrarTipoCambio.html", {"Cambio": cambio})
# Modifica un registro
def vista_cambios_detail(request, cambio_id):
    cambio = SeCatTipoCambio.objects.get(id_tipo_cambio=cambio_id)
    form = FormTipoCambio(instance=cambio)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormTipoCambio(request.POST, instance = cambio)
        if form.is_valid():
            cambio.save() #Guarda cambios
            messages.info(request, "??Tipo de Cambio actualizado con exito!")
            form.save()
            return redirect('vistaCambios') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/ActualizarTipoCambio.html", {"cambio": cambio, "FormTipoCambio" : form}) #envia al detalle de errores
    return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/ActualizarTipoCambio.html", {"cambio": cambio, "FormTipoCambio" : form}) #envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_cambios(View):
    def get(self, request, *args, **kwargs):
        listaCambios=SeCatTipoCambio.objects.filter(status="A") 
        data = {
            'count': listaCambios.count(),
            'cambios': listaCambios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/TipoCambio/listaTiposCambios.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_cambios(View):
    def get(self, request,*args, **kwargs):
        listaCambios=SeCatTipoCambio.objects.filter(status="A") 
        data = {
            'count': listaCambios.count(),
            'cambios': listaCambios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/TipoCambio/listaTiposCambios.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaTiposCambios.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
def export_csv_cambios (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposCambios.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Descripci??n cambio', 'Estatus'])
    listaCambios=SeCatTipoCambio.objects.filter(status="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for lc in listaCambios:
        writer.writerow([lc.id_tipo_cambio, lc.descri_tipocambio, lc.status])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
def export_xlwt_cambios (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposCambios.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tipos de Cambio')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id','Descripci??n cambio','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatTipoCambio.objects.filter(status="A").values_list('id_tipo_cambio','descri_tipocambio','status')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
def listaCambios(request):
    #Lista de todos los paises
    listaCambios=SeCatTipoCambio.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/listaTiposCambios.html", {"cambios":listaCambios})

########################################################### Indicadores ###################################################### xD
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaIndicador(request):
    #Lista de todos los paises que tengan el status = A
    listaIndicador=SeCatIndicador.objects.filter(estatus_ind="A").order_by('id_indicador')
    contador_id = listaIndicador.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaIndicador, 9)
        listaIndicador = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormsIndicador(request.POST) #Valida que sea una peticion de tipo post / Guarda datos
        if form.is_valid():
            indi = form.save(commit=False)
            ultimo_id = SeCatIndicador.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            indi.id_indicador = ultimo_id.id_indicador + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "??El indicador fue agregado con exito!")
            return redirect('VistaIndicadores') #redirecciona a la vista 
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/GestionIndicadores.html",{'entity' : listaIndicador, 'paginator' : paginator, 'FormsIndicador' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_indicador", None)
        print(busqueda)
        if busqueda:
            listaIndicador = SeCatIndicador.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_largo_ind__icontains = busqueda),
                Q(estatus_ind__icontains = "A")
            ).distinct()
    form = FormsIndicador()
    
    data = {
        'entity' : listaIndicador,
        'paginator' : paginator,
        'FormsIndicador' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/GestionIndicadores.html",data)
#Update de estatus de 'A' a 'B' "ELIMINACION"
def eliminarIndicador(request, id_indicador):
    try:
        indi = SeCatIndicador.objects.get(id_indicador=id_indicador)
        indi.estatus_ind = "B"
    except SeCatIndicador.DoesNotExist:
        raise Http404("El indicador no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Indicador eliminado con exito!")
        indi.save()
        return redirect('VistaIndicadores')
    return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/BorrarIndicadores.html", {"Indi": indi})
###modificar
def vista_indicador_detail(request, id_indicador):
    indi = SeCatIndicador.objects.get(id_indicador=id_indicador)
    form = FormsIndicador(instance=indi)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormsIndicador(request.POST, instance=indi)
        if form.is_valid():
            indi.save() #Guarda cambios
            messages.info(request, "??Indicador actualizado con exito!")
            return redirect('VistaIndicadores') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/Actualizarindicadores.html", {"indi": indi, "FormsIndicador" : form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/Actualizarindicadores.html", {"indi": indi, "FormsIndicador" : form})#envia al detalle para actualizar
# vista para "PRINT"
class Export_print_ind(View):
    def get(self, request, *args, **kwargs):
        listaIndi=SeCatIndicador.objects.filter(estatus_ind="A") 
        data = {
            'count': listaIndi.count(),
            'indicadores': listaIndi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/Indicadores/ListarIndicadores.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#PDF
class Export_pdf_indi(View):
    def get(self, request,*args, **kwargs):
        listaIndi=SeCatIndicador.objects.filter(estatus_ind="A") 
        data = {
            'count': listaIndi.count(),
            'indicadores': listaIndi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/Indicadores/ListarIndicadores.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaIndicadores.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises al formato  CSV 
def export_csv_indi (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaIndicadores.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Nombre', 'Abreviatura', 'Estatus', 'Clave de control'])
    listaIndi=SeCatIndicador.objects.filter(estatus_ind="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for indi in listaIndi:
        writer.writerow([indi.id_indicador, indi.descri_largo_ind, indi.descri_corto_ind, indi.estatus_ind, indi.cve_control_ind])
    return response
# Exportar paises a xlwt 
def export_xlwt_indicador (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaIndicador.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicador')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Nombre', 'Abreviatura', 'Estatus', 'Clave de control']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatIndicador.objects.filter(estatus_ind="A").values_list('id_indicador','descri_largo_ind', 'descri_corto_ind', 'estatus_ind', 'cve_control_ind')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
##############################################   PLAN DE ESTUDIOS    #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaPlanE(request):
    #Lista de todos los planes de estudio que tengan el status = A            
    listaPlanE=SeCatPlaEstudio.objects.filter(estatus_plan_est="A").order_by('id_plan_est') 
    contador_id = listaPlanE.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaPlanE, 6)
        listaPlanE = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormsPlaE(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            ultimo_id = SeCatPlaEstudio.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            plan.id_plan_est = ultimo_id.id_plan_est + 1 # agrega uno al ultimo id insertado:
            form.save()
            messages.success(request, "??Plan agregado con exito!") 
            return redirect('vistaPlaneEstudios')#redirecciona a la vista
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/planEstudio/planEstudios/GestionPE.html",{'entity' : listaPlanE, 'paginator' : paginator, 'FormsPlaE' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method =='GET':
        busqueda = request.GET.get("search_planE", None)
        print(busqueda)
        if busqueda:
            listaPlanE = SeCatPlaEstudio.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(decri_larga_plan_est__icontains = busqueda),
                Q(estatus_plan_est__icontains = "A")
            ).distinct()
    form = FormsPlaE()
    data = {
        'entity' : listaPlanE,
        'paginator' : paginator,
        'FormsPlaE' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/planEstudio/planEstudios/GestionPE.html",data)
# Update de estatus de 'A' a 'B' "ELIMINACION"
def eliminarPlan(request, id_plan_est):
    try:
        plan = SeCatPlaEstudio.objects.get(id_plan_est=id_plan_est)
        plan.estatus_plan_est = "B"
    except SeCatPlaEstudio.DoesNotExist:
        raise Http404("El plan no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Plan eliminado con exito!")
        plan.save()
        return redirect('vistaPlaneEstudios')
    return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/BorrarPE.html", {"Plan": plan})
# Modificar 
def vista_planE_detail(request, plan_est_id):
    plan = SeCatPlaEstudio.objects.get(id_plan_est=plan_est_id)
    form = FormsPlaE(instance=plan)
    if request.method == 'POST': #Sobre escribe los valores
        form= FormsPlaE(request.POST, instance=plan) 
        plan.save() #Guarda cambios
        if form.is_valid():
            messages.info(request, "??Plan actualizado con exito!")
            form.save()
            return redirect('vistaPlaneEstudios') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/ActualizarPE.html", {"plan": plan, "FormsPlaE": form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/ActualizarPE.html", {"plan": plan, "FormsPlaE": form})#envia al detalle para actualizar
# vista para imprimir pdf 
class Export_print_planE(View):
    def get(self, request, *args, **kwargs):
        listaPlan=SeCatPlaEstudio.objects.filter(estatus_plan_est="A") 
        data = {
            'count': listaPlan.count(),
            'planes': listaPlan
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/planEstudios/ListarPE.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#ESTA SI JALA COMO PDF NO LAS MAMADAS DE ARRIBA :D
class Export_pdf_planE(View):
    def get(self, request,*args, **kwargs):
        listaPlan=SeCatPlaEstudio.objects.filter(estatus_plan_est="A") 
        data = {
            'count': listaPlan.count(),
            'planes': listaPlan
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/planEstudios/ListarPE.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaPlanesEstudio.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises al formato  CSV 
def export_csv_planE (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaPlanesEstudio.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Nombre', 'Abreviatura', 'Estatus', 'Fecha de alta', 'Modificado por', 'Fecha de baja', 'Modificado por'])
    listaPlanE=SeCatPlaEstudio.objects.filter(estatus_plan_est="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for plan in listaPlanE:
        writer.writerow([plan.id_plan_est, plan.decri_larga_plan_est, plan.descri_corta_plan_est, plan.estatus_plan_est,
                            plan.fec_alta_estpla, plan.user_alta_estpla, plan.fec_baja_estpla, plan.user_baja_estpla])
    return response
# Exportar paises a xlwt 
def export_xlwt_plan (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaPlanesEstudio.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Plan')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Nombre', 'Abreviatura', 'Estatus', 'Fecha de alta', 'Modificado', 'Fecha de baja', 'Modificar']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatPlaEstudio.objects.filter(estatus_plan_est="A").values_list('id_plan_est','decri_larga_plan_est', 'descri_corta_plan_est', 'estatus_plan_est',
                                                                            'fec_alta_estpla', 'user_alta_estpla', 'fec_baja_estpla', 'user_baja_estpla')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
##############################################   GRADOS    ####################################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
def vistaGrados(request):
    #Lista de todos los planes de estudio que tengan el status = A            
    listaGrados=SeCatGrado.objects.filter(estatus_gra="A").order_by('id_grado') 
    contador_id = listaGrados.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaGrados, 6)
        listaGrados = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormsGrados(request.POST)
        if form.is_valid():
            grado = form.save(commit=False)
            ultimo_id = SeCatGrado.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            grado.id_grado = ultimo_id.id_grado + 1 # agrega uno al ultimo id insertado:
            form.save()
            messages.success(request, "??Grado agregado con exito!")
            return redirect('vistaGrados')#redirecciona a la vista 
        else:
            messages.warning(request, "??Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Grados/GestionGrados.html",{ 'entity' : listaGrados, 'paginator' : paginator, 'FormsGrados' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method =='GET':
        busqueda = request.GET.get("search_grados", None)
        print(busqueda)
        if busqueda:
            listaGrados = SeCatGrado.objects.filter(
                #Revisi??n de los campos de la tabla en la BD
                Q(descri_corto_gra__icontains = busqueda),
                Q(estatus_gra__icontains = "A")
            ).distinct()
    form = FormsGrados()
    data = {
        'entity' : listaGrados,
        'paginator' : paginator,
        'FormsGrados' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/Grados/GestionGrados.html",data)
# Update de estatus de 'A' a 'B' "ELIMINACION"
def eliminarGrado(request, id_grado):
    try:
        grado = SeCatGrado.objects.get(id_grado=id_grado)
        grado.estatus_gra = "B"
    except SeCatGrado.DoesNotExist:
        raise Http404("El Grado no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "??Grado eliminado con exito!")
        grado.save()
        return redirect('vistaGrados')
    return render(request, "controlEscolar/catalogos/estudiantes/Grados/BorrarGrado.html", {"Grado": grado})
# Modificar 
def vista_grados_detail(request, grado_id):
    grado = SeCatGrado.objects.get(id_grado=grado_id)
    form = FormsGrados(instance=grado)
    if request.method == 'POST': #Sobre escribe los valores
        form= FormsGrados(request.POST, instance=grado) 
        grado.save() #Guarda cambios
        if form.is_valid():
            messages.info(request, "??Grado actualizado con exito!")
            form.save()
            return redirect('vistaGrados') #retorna despues de actualizar
        else:
            return render(request, "controlEscolar/catalogos/estudiantes/Grados/ActualizarGrado.html", {"grado": grado, "FormsGrados": form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/estudiantes/Grados/ActualizarGrado.html", {"grado": grado, "FormsGrados": form})#envia al detalle para actualizar
# vista para imprimir pdf 
class Export_print_grados(View):
    def get(self, request, *args, **kwargs):
        listaGrado=SeCatGrado.objects.filter(estatus_gra="A") 
        data = {
            'count': listaGrado.count(),
            'grados': listaGrado
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Grados/ListarGrados.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#ESTA SI JALA COMO PDF NO LAS MAMADAS DE ARRIBA :D
class Export_pdf_grado(View):
    def get(self, request,*args, **kwargs):
        listaGrados=SeCatGrado.objects.filter(estatus_gra="A") 
        data = {
            'count': listaGrados.count(),
            'grados': listaGrados
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Grados/listarGrados.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaGrados.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises al formato  CSV 
def export_csv_grados (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaGrados.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Descripci??n', 'Estatus'])
    listaGrado=SeCatGrado.objects.filter(estatus_gra="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for grado in listaGrado:
        writer.writerow([grado.id_grado, grado.descri_corto_gra, grado.estatus_gra])
    return response
# Exportar paises a xlwt 
def export_xlwt_grados (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaGrados.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Grados')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Descripci??n', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatGrado.objects.filter(estatus_gra="A").values_list('id_grado','descri_corto_gra', 'estatus_gra')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
