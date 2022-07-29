# Django
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.contrib import messages
#Insert SQL
from django.db import connections
#Para imprimir en formatos
import csv
import xlwt
# Importa funcion para pdf que se encuentra en el archivo Utils.py
from Apps.controlEscolar.utils import render_to_pdf
#paginador
from django.core.paginator import Paginator
#Search Datos y consultas
from django.db.models import Q
#Login control de inicios de sesion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#Models
from .models import (
    SeCatPais, SeCatEstado, SeCatMunicipioDelegacion, SeCatAsentamiento, SeCatColonia,  # Direcciones
    SeCatUniversidad, SeCatDivision, SeCatCarrera, SeCatPeriodos, # Universidades
    SeCatEscuelaProcedencia, SeCatMedioDifusion, SeCatTipoEscuela, SeCatAreaBachillerato, SeProIndAsp, # Aspirantes
    SeTabEstudiante, SeCatDocumentacion, SeCatGrupo, SeCatEstatusEstudiante, SeCatGrado, SeCatSalones, SeCatTipoBajas, SeCatBecas, SeCatTipoCambio, # Estudintes
    SeCatEmpleado, SeCatNivelAcademico, SeCatPlaza, SeCatTipoPuesto, SeCatSueldos, SeCatDeptoEmp, SeCatActividades, SeCatInstitucion, SeTabEmpCar, # Empleados
    SeCatPlaEstudio, SeCatAsignatura, SeCatIndicador, SeProPlanEstudio, SeProAsiIndicador, # Plan de Estudio
)
#Views
from django.views.generic import View
#formularios
from .forms import (
    FormPaises, FormEstados, FormMunicipiosDelegaciones, FormAsentamiento, FormColonias, # Direcciones
    FormUniversidad, FormDivisiones, FormCarreras, FormPeriodos, # Universidades
    FormEscProc, FormMediosDifusion, FormTiposEscuelas, FormAreaBachi, FormIndAsp, # Aspirantes
    FormsEstudiante, FormDocumentacion, FormGrupo, FormEstatusEstudiante,FormGrados, FormSalones, FormTipoBajas, FormBecas, FormTipoCambio, # Estudintes
    FormEmpleado, FormsTipoPue, FormSueldo, FormNivAca, FormPlaza, FormAdscripcion, FormActividades, FormInstitucion, FormEmpCar, # Empleados
    FormsPlaE, FormsAsignatura, FormsIndicador, FormsPeA, FormsPeaI, # Plan de Estudio
    FormsAspirantes, #Aspirante
)

# -------------------------------------------- Direcciones --------------------------------------------- #

##############################################   Paises   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
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
            pais = form.save(commit=False)
            ultimo_id = SeCatPais.objects.all().order_by('rowid_pais').last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            pais.rowid_pais = ultimo_id.rowid_pais + 1 # agrega uno al ultimo id insertado
            pais.save() # en este caso guarda todos los datos del formulario por que ingresamos el id pero en los fomularios que el id sea automatico cambia
            messages.success(request, "¡Pais agregado con exito!") # Manda un mensaje al usuario desdes de que todos los datos son correctos, solo funciona con success(Verde), warning(Amarilla), info(Azul)      
            return redirect('vista_paises') #redirecciona a la vista de nuevo
        else: # En caso de que alguno de los campos no sean correctos entra en el else y redirecciona al mismo formulario con los datos no correctos y por que no son correctos
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/GestionPaises.html",{'entity' : listaPaises,'paginator' : paginator,'FormPaises' : form,'contador': contador_id})       
    #Busqueda del search
    elif request.method == 'GET': #Valida que sea una peticion del form sea de tipo GET para poder realizar la busqueda de los datos
        busqueda = request.GET.get("search_paises", None) # En la variable guarda lo que se obtuvo de la barra de gusqueda
        if busqueda: # Si trae datos entra al if para poder hacer la consulta 
            listaPaises = SeCatPais.objects.filter( #Revisión de los campos de la tabla en la BD
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
@login_required
def eliminarPais(request, rowid_pais):
    try:
        pais = SeCatPais.objects.get(rowid_pais=rowid_pais)
        pais.estatus_pais = "B"
    except SeCatPais.DoesNotExist:
        raise Http404("El pais no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "¡Pais eliminado con exito!")
        pais.save()
        return redirect('vista_paises')
    return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/BorrarPais.html", {"Pais": pais})
# Modifica un registro
@login_required
def vista_paises_detail(request, rowid_pais):
    pais = SeCatPais.objects.get(rowid_pais=rowid_pais)
    form = FormPaises(instance=pais)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormPaises(request.POST, instance = pais)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "¡Pais actualizado con exito!")
            return redirect('vista_paises') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/ActualizarPais.html", {"pais": pais, "FormPaises" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/ActualizarPais.html", {"pais": pais, "FormPaises" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_paises(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
        data = {
            'count': listaPaises.count(),
            'paises': listaPaises
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionPaises/listaPaises.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_paises(LoginRequiredMixin, View):
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
@login_required
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
@login_required
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
@login_required
def listaPaises(request):
    #Lista de todos los paises
    listaPaises=SeCatPais.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/direcciones/GestionPaises/listaPaises.html", {"paises":listaPaises})

##############################################   Estados   ########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaEstados(request):
    listaEstados=SeCatEstado.objects.filter(estatus_edo="A").order_by('rowid_edo')#Lista de todos los paises que tengan el status = A
    contador_id = listaEstados.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaEstados, 9)
        listaEstados = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormEstados(request.POST)
        if form.is_valid():
            estado = form.save(commit=False)
            ultimo_id = SeCatEstado.objects.all().order_by('rowid_edo').last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            estado.rowid_edo = ultimo_id.rowid_edo + 1 # agrega uno al ultimo id insertado
            estado.save() # en este caso guarda todos los datos del formulario por que ingresamos el id pero en los fomularios que el id sea automatico cambia
            messages.success(request, "¡Estado agregado con exito!")
            return redirect('vista_estados') #redirecciona a la vista 
        else:
            messages.success(request, "¡Grado agregado con exito!")
            return render(request, "controlEscolar/catalogos/direcciones/GestionEstados/GestionEstados.html",{'entity' : listaEstados, 'paginator' : paginator, 'FormEstados' : form, 'contador' : contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_estados", None)
        print(busqueda)
        if busqueda:
            listaEstados = SeCatEstado.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(descri_largo_edo__icontains = busqueda),
	            Q(estatus_edo__icontains = "A")
            ).distinct()
    form = FormEstados()
    data = {
        'entity' : listaEstados,
        'paginator' : paginator,
        'FormEstados' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/direcciones/GestionEstados/GestionEstados.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarEstado(request, rowid_edo):
    try:
        estado = SeCatEstado.objects.get(rowid_edo=rowid_edo)
        estado.estatus_edo = "B"
    except SeCatEstado.DoesNotExist:
        raise Http404("El Estado no existe")
    if request.method == 'POST': #Sobre escrive los valores
        estado.save()
        messages.warning(request, "¡Estado eliminado con exito!")
        return redirect('vista_estados')
    return render(request, "controlEscolar/catalogos/direcciones/GestionEstados/BorrarEstado.html", {"Estado": estado})
# Modifica un registro
@login_required
def vista_estados_detail(request, rowid_edo):
    estado = SeCatEstado.objects.get(rowid_edo=rowid_edo)
    form = FormEstados(instance=estado)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormEstados(request.POST, instance = estado)
        if form.is_valid():
            est = form.save(commit=False)   
            est.save()
            messages.info(request, "¡Estado actualizado con exito!")
            return redirect('vista_estados') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/direcciones/GestionEstados/ActualizarEstado.html", {"FormEstados" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/direcciones/GestionEstados/ActualizarEstado.html", {"FormEstados" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_estados(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaEstados=SeCatEstado.objects.filter(estatus_edo="A") 
        data = {
            'count': listaEstados.count(),
            'estados': listaEstados
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionEstados/listaEstados.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_estados(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaEstados=SeCatEstado.objects.filter(estatus_edo="A") 
        data = {
            'count': listaEstados.count(),
            'estados': listaEstados
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionEstados/listaEstados.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaEstados.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_estados (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaEstados.csv;'
    writer = csv.writer(response)
    writer.writerow(['Pais','Clave','Estado','Abreviacion','Estatus'])
    listaEstados=SeCatEstado.objects.filter(estatus_edo="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for estado in listaEstados:
        writer.writerow([estado.rowid_pais.descri_largo_pais, estado.id_edo, estado.descri_largo_edo, estado.descri_corto_edo, estado.estatus_edo])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_estados (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaEstados.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Estados')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Pais','Clave','Estado','Abreviacion','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatEstado.objects.filter(estatus_edo="A").values_list('rowid_pais', 'id_edo', 'descri_largo_edo', 'descri_corto_edo', 'estatus_edo')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
@login_required
def listaEstados(request):
    #Lista de todos los paises
    listaEstados=SeCatEstado.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/direcciones/GestionEstados/listaEstados.html", {"estados":listaEstados})

##############################################   Municipios/Delegaciones   ###########################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaMunicipios(request):
    #Lista de todos los paises que tengan el status = A
    listaMunicipios=SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A").order_by('id_mundel')
    contador_id = listaMunicipios.count()
    listaPais = SeCatPais.objects.filter(estatus_pais="A").order_by('id_pais')
    listaEstado = SeCatEstado.objects.filter(estatus_edo="A").order_by('id_edo')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaMunicipios, 9)
        listaMunicipios = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormMunicipiosDelegaciones(request.POST)
        if form.is_valid():
            mun = form.save(commit=False)
            ultimo_id = SeCatMunicipioDelegacion.objects.all().order_by('rowid_mundel').last()
            mun.rowid_mundel = ultimo_id.rowid_mundel + 1
            mun.save()
            messages.success(request, "¡Municipio/Delegación agregado con exito!")
            return redirect('vista_municipios')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/direcciones/GestionMunicipios/GestionMunicipios.html",{'entity' : listaMunicipios, 'paginator' : paginator, 'FormMunicipiosDelegaciones' : form, 'contador' : contador_id, 'listaPais':listaPais, 'listaEstado':listaEstado})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_municipios", None)
        print(busqueda)
        if busqueda:
            listaMunicipios = SeCatMunicipioDelegacion.objects.filter( #Revisión de los campos de la tabla en la BD
                Q(descri_largo_mundel__icontains = busqueda),
	            Q(estatus_mundel__icontains = "A")
            ).distinct()
    form = FormMunicipiosDelegaciones()
    data = {
        'entity' : listaMunicipios,
        'paginator' : paginator,
        'FormMunicipiosDelegaciones' : form,
        'contador' : contador_id,
        'listaPais' : listaPais,
        'listaEstado' : listaEstado,
    }
    return render(request, "controlEscolar/catalogos/direcciones/GestionMunicipios/GestionMunicipios.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarMunicipio(request, rowid_mundel):
    try:
        mundel = SeCatMunicipioDelegacion.objects.get(rowid_mundel = rowid_mundel)
        mundel.estatus_mundel = "B"
    except SeCatMunicipioDelegacion.DoesNotExist:
        raise Http404("El Municipio no existe")
    if request.method == 'POST': #Sobre escrive los valores
        mundel.save()
        messages.warning(request, "¡Municipio/Delegación eliminado con exito!")
        return redirect('vista_municipios')
    return render(request, "controlEscolar/catalogos/direcciones/GestionMunicipios/BorrarMunicipio.html", {"Municipio": mundel})
# Modifica un registro
@login_required
def vista_municipios_detail(request, rowid_mundel):
    mundel = SeCatMunicipioDelegacion.objects.get(rowid_mundel = rowid_mundel)
    form = FormMunicipiosDelegaciones(instance=mundel)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormMunicipiosDelegaciones(request.POST, instance = mundel)
        if form.is_valid():
            mun = form.save(commit=False)   
            mun.save()
            messages.info(request, "¡Municipio/Delegación actualizado con exito!")
            return redirect('vista_municipios')  #retorna despues de actualizar              
        else: 
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/direcciones/GestionMunicipios/ActualizarMunicipio.html", {"FormMunicipiosDelegaciones" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/direcciones/GestionMunicipios/ActualizarMunicipio.html", {"FormMunicipiosDelegaciones" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_municipios(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaMunicipios=SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A") 
        data = {
            'count': listaMunicipios.count(),
            'municipios': listaMunicipios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionMunicipios/listaMunicipios.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_municipios(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaMunicipios=SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A") 
        data = {
            'count': listaMunicipios.count(),
            'municipios': listaMunicipios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionMunicipios/listaMunicipios.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaMunicipios.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar municipio/delegaciones a CSV sin libreria 
@login_required
def export_csv_municipios (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaMunicipios.csv;'
    writer = csv.writer(response)
    writer.writerow(['Estado','Clae','Municipio/Delegación','Abreviatura','Estatus'])
    listaMunicipios=SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for municipio in listaMunicipios:
        writer.writerow([municipio.rowid_edo.descri_largo_edo, municipio.id_mundel, municipio.descri_largo_mundel, municipio.descri_corto_mundel, municipio.estatus_mundel])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_municipios (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaMunicipios.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Municipios')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id Pais','Id Estado','Id Municipio/Delegacion','Municipio/Delegación','Abreviatura','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A").values_list('rowid_edo', 'id_mundel','descri_largo_mundel','descri_corto_mundel','estatus_mundel')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
@login_required
def listaMunicipios(request):
    #Lista de todos los paises
    listaMunicipios=SeCatMunicipioDelegacion.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/direcciones/GestionMunicipios/listaMunicipios.html", {"municipios":listaMunicipios})

##############################################   Asentamiento   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaAsen(request):
    listaAsen = SeCatAsentamiento.objects.filter(estatus_asentamiento="A").order_by('rowid_asentamiento')
    contador_id = listaAsen.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaAsen, 7)
        listaAsen = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormAsentamiento(request.POST)
        if form.is_valid():
            asen = form.save(commit=False)
            ultimo_id = SeCatAsentamiento.objects.all().order_by('rowid_asentamiento').last()
            asen.rowid_asentamiento = ultimo_id.rowid_asentamiento + 1
            asen.save()
            messages.success(request, "¡Asentamiento agregado con exito!")
            return redirect('vista_asen')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/direcciones/GestionAsentamiento/GestionAsentamiento.html",{'entity' : listaAsen,'paginator' : paginator,'FormAsentamiento' : form,'contador': contador_id})
    elif request.method == 'GET':
        busqueda = request.GET.get("search_asen", None)
        if busqueda:
            listaAsen = SeCatAsentamiento.objects.filter(
                Q(descri_largo_asentamiento__icontains = busqueda),
                Q(estatus_asentamiento__icontains = "A")
            ).distinct()
    form = FormAsentamiento()
    data = {
        'entity' : listaAsen,
        'paginator' : paginator,
        'FormAsentamiento' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/direcciones/GestionAsentamiento/GestionAsentamiento.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarAsen(request, rowid_asentamiento):
    try:
        asen = SeCatAsentamiento.objects.get(rowid_asentamiento = rowid_asentamiento)
        asen.estatus_asentamiento = "B"
    except SeCatAsentamiento.DoesNotExist:
        raise Http404("El Asentamiento no existe")
    if request.method == 'POST': #Sobre escrive los valores
        asen.save()
        messages.warning(request, "¡Asentamiento eliminado con exito!")
        return redirect('vista_asen')
    return render(request, "controlEscolar/catalogos/direcciones/GestionAsentamiento/BorrarAsentamiento.html", {"Asen": asen})
# Modifica un registro
@login_required
def vista_asen_detail(request, rowid_asentamiento):
    asen = SeCatAsentamiento.objects.get(rowid_asentamiento = rowid_asentamiento)
    form = FormAsentamiento(instance=asen)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormAsentamiento(request.POST, instance = asen)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "¡Asentamiento actualizado con exito!")
            return redirect('vista_asen') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/direcciones/GestionAsentamiento/ActualizarAsentamiento.html", {"FormAsentamiento" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/direcciones/GestionAsentamiento/ActualizarAsentamiento.html", {"FormAsentamiento" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_asen(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaAsen = SeCatAsentamiento.objects.filter(estatus_asentamiento="A")
        data = {
            'count': listaAsen.count(),
            'asen': listaAsen
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionAsentamiento/ListaAsen.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_asen(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaAsen = SeCatAsentamiento.objects.filter(estatus_asentamiento="A")
        data = {
            'count': listaAsen.count(),
            'asen': listaAsen
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionAsentamiento/ListaAsen.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Lista Asentamientos.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria
@login_required
def export_csv_asen (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=Lista Asentamientos.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave', 'Asentamiento','Abreviacion', 'Estatus'])
    listaAsen = SeCatAsentamiento.objects.filter(estatus_asentamiento="A")
    for a in listaAsen:
        writer.writerow([a.id_asentamiento, a.descri_largo_asentamiento, a.descri_corto_asentamiento, a.estatus_asentamiento])
    return response
# Exportar paises a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_asen (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=Lista Asentamiento.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Asentamiento')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave','Asentamiento','Abreviacion', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatAsentamiento.objects.filter(estatus_asentamiento="A").values_list('id_asentamiento', 'descri_largo_asentamiento','descri_corto_asentamiento', 'estatus_asentamiento')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################################   Colonias   #####################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaColonias(request):
    #Lista de todos los paises que tengan el status = A
    listaColonias=SeCatColonia.objects.filter(estatus_col="A").order_by('id_col')
    contador_id = listaColonias.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaColonias, 6)
        listaColonias = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormColonias(request.POST)
        if form.is_valid():
            colo = form.save(commit=False)
            ultimo_id = SeCatColonia.objects.all().order_by('rowid_col').last()
            colo.rowid_col = ultimo_id.rowid_col + 1
            colo.save()
            messages.success(request, "¡Colonia agregada con exito!")
            return redirect('vistaColonias') #redirecciona a la vista 
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/direcciones/GestionColonias/GestionColonias.html",{'entity' : listaColonias, 'paginator' : paginator, 'FormColonias' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_colonias", None)
        print(busqueda)
        if busqueda:
            listaColonias = SeCatColonia.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(descri_largo_col__icontains = busqueda),
                Q(estatus_col__icontains = "A")
            ).distinct()
    form = FormColonias()
    data = {
        'entity' : listaColonias,
        'paginator' : paginator,
        'FormColonias' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/direcciones/GestionColonias/GestionColonias.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarColonia(request, rowid_col):
    try:
        colonia = SeCatColonia.objects.get(rowid_col = rowid_col)
        colonia.estatus_col = "B"
    except SeCatColonia.DoesNotExist:
        raise Http404("La Colonia no existe")
    if request.method == 'POST': #Sobre escrive los valores
        colonia.save()
        messages.warning(request, "¡Colonia eliminada con exito!")
        return redirect('vistaColonias')
    return render(request, "controlEscolar/catalogos/direcciones/GestionColonias/BorrarColonia.html", {"Colonia": colonia})
# Modifica un registro
@login_required
def vista_colonias_detail(request, rowid_col):
    colonia = SeCatColonia.objects.get(rowid_col = rowid_col)
    form = FormColonias(instance=colonia)
    if request.method == 'POST':
        form = FormColonias(request.POST, instance = colonia)
        if form.is_valid():
            form.save()
            messages.info(request, "¡Colonia actualizada con exito!")
            return redirect('vistaColonias') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/direcciones/GestionColonias/ActualizarColonia.html", {"FormColonias" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/direcciones/GestionColonias/ActualizarColonia.html", {"FormColonias" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_colonias(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaColonias=SeCatColonia.objects.filter(estatus_col="A") 
        data = {
            'count': listaColonias.count(),
            'colonias': listaColonias
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionColonias/listaColonias.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_colonias(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaColonias=SeCatColonia.objects.filter(estatus_col="A") 
        data = {
            'count': listaColonias.count(),
            'colonias': listaColonias
        }
        pdf = render_to_pdf('controlEscolar/catalogos/direcciones/GestionColonias/listaColonias.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaColonias.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_colonias (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaColonias.csv'
    writer = csv.writer(response)
    writer.writerow(['Municipio/Delegación', 'Asentamiento','Clave', 'Colonia', 'Abreviatura', 'Codigo Postal', 'Estatus'])
    listaColonias=SeCatColonia.objects.filter(estatus_col="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for col in listaColonias:
        writer.writerow([col.rowid_mundel.descri_largo_mundel, col.rowid_asentamiento.descri_largo_asentamiento ,col.id_col, col.descri_largo_col, col.descrip_corto_col, col.codposcol, col.estatus_col])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_colonias (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaColonias.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Colonias')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Municipio/Delegación', 'Asentamiento','Clave', 'Colonia', 'Abreviatura', 'Codigo Postal', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatColonia.objects.filter(estatus_col="A").values_list('rowid_mundel', 'rowid_asentamiento','id_col', 'descri_largo_col', 'descrip_corto_col', 'codposcol', 'estatus_col')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response
# Vista de pre-visualizacion PFD solo es para pruebas
@login_required
def listaColonias(request):
    #Lista de todos los paises
    listaColonias=SeCatColonia.objects.all()
    # Filtrando por estatus
    # listaPaises=SeCatPais.objects.filter(estatus_pais="A") 
    return render(request, "controlEscolar/catalogos/direcciones/GestionColonias/listaColonias.html", {"colonias":listaColonias})

# -------------------------------------------- Universidad --------------------------------------------- #

##############################################   Universidades   ##################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaUniversidades(request):
    #Lista de todas las universidades
    listaUniversidades=SeCatUniversidad.objects.filter(estatus_uni="A").order_by('rowid_uni')
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
            uni.rowid_uni = ultimo_id.rowid_uni + 1 # agrega uno al ultimo id insertado
            uni.save()
            messages.success(request, "¡Universidad agregada con exito!")
            #redirecciona a la vista
            return redirect('vista_universidades')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/GestionUniversidades.html",{'entity' : listaUniversidades,'paginator' : paginator, 'FormUniversidad' : form,'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_universidades", None)
        print(busqueda)
        if busqueda:
            listaUniversidades = SeCatUniversidad.objects.filter(
                #Revisión de los campos de la tabla en la BD
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
@login_required
def eliminarUniversidad(request, rowid_uni):
    try:
        uni = SeCatUniversidad.objects.get(rowid_uni=rowid_uni)
        uni.estatus_uni = "B"
    except SeCatUniversidad.DoesNotExist:
        raise Http404("La Universidad no existe")
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "¡Universidad eliminada con exito!")
        uni.save()
        return redirect('vista_universidades')
    return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/BorrarUniversidades.html", {"Universidad": uni})
# Modifica un registro
@login_required
def vista_universidad_detail(request, rowid_uni):
    uni = SeCatUniversidad.objects.get(rowid_uni=rowid_uni)
    form = FormUniversidad(instance = uni)
    if request.POST: #Sobre escribe los valores
        form = FormUniversidad(request.POST, instance = uni)
        if form.is_valid():
            messages.info(request, "¡Universidad actualizada con exito!")
            form.save()
            return redirect('vista_universidades') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/ActualizarUniversidad.html", {"FormUniversidad" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/universidad/GestionUniversidades/ActualizarUniversidad.html", {"FormUniversidad" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir
class Export_print_universidades(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaUniversidades = SeCatUniversidad.objects.filter(estatus_uni="A")
        data = {
            'count': listaUniversidades.count(),
            'uni': listaUniversidades
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionUniversidades/listaUniversidades.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Universidades
class Export_pdf_universidades(LoginRequiredMixin, View):
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
@login_required
def export_csv_universidades (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaUniversidades.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Id Colonia', 'Id Universidad', 'Nombre universidad', 'Tipo de organización', 'Dirección',
                    'RFC', 'Cod. Pos.', 'Tel 1', 'Tel 2', 'Tel 3', 'Ext 1', 'Ext 2', 'Ext 3', 'Email', 'Pag. Internet', 'Contacto', 'Estatus'])
    listaUniversidades=SeCatUniversidad.objects.filter(estatus_uni="A")
    for uni in listaUniversidades:
        writer.writerow([uni.rowid_uni, uni.rowid_col, uni.id_uni, uni.nombre_uni, uni.tipo_org_uni, uni.direccion_uni, uni.rfc_uni,
                        uni.codpos_uni, uni.telefono1_uni, uni.telefono2_uni, uni.telefono3_uni, uni.ext1_uni,
                        uni.ext2_uni, uni.ext3_uni, uni.mail_uni, uni.pagina_internet_uni, uni.contacto_uni, uni.estatus_uni])
    return response
# Exportar universidades a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_universidades (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaUniversidades.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Universidades')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Id Colonia', 'Id Universidad', 'Nombre universidad', 'Tipo de organización', 'Dirección',
                'RFC', 'Cod. Pos.', 'Tel 1', 'Tel 2', 'Tel 3','Ext 1', 'Ext 2', 'Ext 3', 'Email', 'Pag. Internet', 'Contacto', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatUniversidad.objects.filter(estatus_uni="A").values_list('rowid_uni', 'rowid_col', 'id_uni', 'nombre_uni', 'tipo_org_uni', 'direccion_uni', 'rfc_uni',
                        'codpos_uni', 'telefono1_uni', 'telefono2_uni', 'telefono3_uni','ext1_uni',
                        'ext2_uni', 'ext3_uni', 'mail_uni', 'pagina_internet_uni', 'contacto_uni', 'estatus_uni')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################  DIVISIÓN  ##################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_Divisiones(request):
    listaDivisiones = SeCatDivision.objects.filter(estatus_div="A").order_by('rowid_div')
    contador_id = listaDivisiones.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaDivisiones, 9)
        listaDivisiones = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormDivisiones(request.POST)
        if form.is_valid():
            div = form.save(commit=False)
            ultimo_id = SeCatDivision.objects.all().order_by('rowid_div').last()
            div.rowid_div = ultimo_id.rowid_div + 1
            div.save()
            messages.success(request, "¡División agregada con exito!")
            return redirect('vista_Divisiones')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/universidad/GestionDivisiones/GestionDivisiones.html",{'entity' : listaDivisiones, 'paginator' : paginator, 'FormDivisiones' : form, 'contador': contador_id,})       
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_divisiones", None)
        print(busqueda)
        if busqueda:
            listaDivisiones = SeCatDivision.objects.filter(
                Q(descri_larga_div__icontains = busqueda),
                Q(estatus_div__icontains = "A")
            ).distinct()
    form = FormDivisiones()
    data = {
        'entity' : listaDivisiones,
        'paginator' : paginator,
        'FormDivisiones' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/universidad/GestionDivisiones/GestionDivisiones.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminar_Divisiones(request, rowid_div):
    try:
        div = SeCatDivision.objects.get(rowid_div=rowid_div)
        div.estatus_div = "B"
    except SeCatDivision.DoesNotExist:
        raise Http404("La División no existe")
    if request.method == 'POST':
        div.save()
        messages.warning(request, "¡División eliminada con exito!")
        return redirect('vista_Divisiones')
    return render(request, "controlEscolar/catalogos/universidad/GestionDivisiones/BorrarDivisiones.html", {"Division": div})
# Modifica un registro
@login_required
def vista_divisiones_detail(request, rowid_div):
    div = SeCatDivision.objects.get(rowid_div=rowid_div)
    form = FormDivisiones(instance = div)
    if request.method == 'POST':
        form = FormDivisiones(request.POST, instance = div)
        if form.is_valid():
            divi = form.save(commit=False)
            divi.save()
            messages.info(request, "¡División actualizada con exito!")
            return redirect('vista_Divisiones')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/universidad/GestionDivisiones/ActualizarDivisiones.html", {"FormDivisiones" : form})
    return render(request, "controlEscolar/catalogos/universidad/GestionDivisiones/ActualizarDivisiones.html", {"FormDivisiones" : form})
# primera de pdf posible imprimir 
class Export_print_divisiones(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaDivisiones = SeCatDivision.objects.filter(estatus_div="A")
        data = {
            'count': listaDivisiones.count(),
            'div': listaDivisiones
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionDivisiones/listaDivisiones.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Divisiones
class Export_pdf_divisiones(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaDivisiones=SeCatDivision.objects.filter(estatus_div="A")
        data = {
            'count': listaDivisiones.count(),
            'div': listaDivisiones
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionDivisiones/listaDivisiones.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaDivisiones.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria
@login_required
def export_csv_divisiones (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaDivisiones.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id Universidad','Clave División','Nombre División','Abreviación División','Representante','Tel 1','Tel 2','Ext 1','Ext 2','Email','Estatus'])
    listaDivisiones=SeCatDivision.objects.filter(estatus_div="A")
    for div in listaDivisiones:
        writer.writerow([div.rowid_uni, div.id_div, div.descri_larga_div, div.descri_corta_div, div.representante_div,
                        div.telefono_1_div, div.telefono_2_div, div.extension1_div, div.extension2_div,
                        div.mail_div, div.estatus_div])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_divisiones (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaDivisiones.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Divisiones')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id Universidad','Clave División','Nombre División','Abreviación','Representante','Tel 1','Tel 2','Ext 1','Ext 2','Email','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatDivision.objects.filter(estatus_div="A").values_list('rowid_uni','id_div','descri_larga_div','descri_corta_div',
                                                                    'representante_div','telefono_1_div','telefono_2_div',
                                                                    'extension1_div','extension2_div','mail_div','estatus_div')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################   Carreras   ##########################################################

#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaCarreras(request):
    #Lista de todas las divisiones
    listaCarreras = SeCatCarrera.objects.filter(estatus_car="A").order_by('rowid_car')
    contador_id = listaCarreras.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaCarreras, 4)
        listaCarreras = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormCarreras(request.POST)
        if form.is_valid():
            carr=form.save(commit=False)
            ultimo_id = SeCatCarrera.objects.all().order_by('rowid_car').last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            carr.rowid_car = ultimo_id.rowid_car + 1 # agrega uno al ultimo id insertado
            carr.save()
            messages.success(request, "¡Carrera agregada con exito!")
            #redirecciona a la vista 
            return redirect('vista_carreras')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/universidad/GestionCarreras/GestionCarreras.html",{'entity' : listaCarreras, 'paginator' : paginator, 'FormCarreras' : form, 'contador': contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_carreras", None)
        if busqueda:
            listaCarreras = SeCatCarrera.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(descri_largo_car__icontains = busqueda),
                Q(estatus_car__icontains = "A") 
            ).distinct()
    form = FormCarreras()
    data = {
        'entity' : listaCarreras,
        'paginator' : paginator,
        'FormCarreras' : form,
        'contador': contador_id,
    }
    return render(request,"controlEscolar/catalogos/universidad/GestionCarreras/GestionCarreras.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarCarreras(request, rowid_car):
    try:
        car = SeCatCarrera.objects.get(rowid_car=rowid_car)
        car.estatus_car = "B"
    except SeCatCarrera.DoesNotExist:
        raise Http404("La Carrera no existe")
    if request.method == 'POST': #Sobre escrive los valores
        car.save()
        messages.warning(request, "¡Carrera eliminada con exito!")
        return redirect('vista_carreras')
    return render(request, "controlEscolar/catalogos/universidad/GestionCarreras/BorrarCarreras.html", {"Carrera": car})
@login_required
def vista_carreras_detail(request, rowid_car ):
    car = SeCatCarrera.objects.get(rowid_car=rowid_car)
    form = FormCarreras(instance=car)
    if request.method == 'POST': #Sobre escribe los valores
        form = FormCarreras(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.info(request, "¡Carrera actualizada con exito!")
            return redirect('vista_carreras') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/universidad/GestionCarreras/ActualizaCarreras.html", {"FormCarreras" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/universidad/GestionCarreras/ActualizaCarreras.html", {"FormCarreras" : form})#envia al detalle para actualizar
#Imprimir
class Export_print_carreras(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaCarreras = SeCatCarrera.objects.filter(estatus_car="A") 
        data = {
            'count': listaCarreras.count(),
            'car': listaCarreras
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionCarreras/listaCarreras.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_carreras(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaCarreras=SeCatCarrera.objects.filter(estatus_car="A") 
        data = {
            'count': listaCarreras.count(),
            'car': listaCarreras
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionCarreras/listaCarreras.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaCarreras.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria
@login_required 
def export_csv_carreras (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaCarreras.csv;'
    writer = csv.writer(response)
    writer.writerow(['ID Division', 'ID Carrera' , 'Nombre Carrera', 'Abreviacion',
                    'Descripcion', 'Ceneval', 'Estatus'])
    listaCarreras=SeCatCarrera.objects.filter(estatus_car="A") 
    for car in listaCarreras:
        writer.writerow([car.rowid_div.descri_larga_div, car.id_car ,car.descri_largo_car, car.descri_corto_car, car.descri_largo_tit,
                        car.ceneval_car, car.estatus_car])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT
@login_required 
def export_xlwt_carreras (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaCarreras.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Carreras')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['ID Division', 'ID Carrera', 'Nombre Carrera', 'Abreviacion', 'Descripcion',
                'Ceneval', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatCarrera.objects.filter(estatus_car="A").values_list('rowid_div', 'id_car', 'descri_largo_car', 
                                                                'descri_corto_car', 'descri_largo_tit', 'ceneval_car', 'estatus_car')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################### Periodos #################################################
# #Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaPeriodos(request):
    #Lista de todas las divisiones
    listaPer = SeCatPeriodos.objects.filter(estatus_per="A").order_by('evento_per')
    contador_id = listaPer.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaPer, 9)
        listaPer = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormPeriodos(request.POST)
        if form.is_valid():
            per = form.save(commit=False)
            ultimo_id = SeCatPeriodos.objects.all().order_by('rowid_per').last()
            per.rowid_per = ultimo_id.rowid_per + 1
            per.save()
            messages.success(request, "¡Periodo agregado con exito!")
            #redirecciona a la vista 
            return redirect('vista_periodos')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/universidad/GestionPeriodos/GestionPeriodos.html",{'entity' : listaPer, 'paginator' : paginator, 'FormPeriodos' : form, 'contador': contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_periodos", None)
        if busqueda:
            listaPer = SeCatPeriodos.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(evento_per__icontains = busqueda),
                Q(estatus_per__icontains = "A")
            ).distinct()
    form = FormPeriodos()
    data = {
        'entity' : listaPer,
        'paginator' : paginator,
        'FormPeriodos' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/universidad/GestionPeriodos/GestionPeriodos.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarPeriodo(request, rowid_per):
    try:
        per = SeCatPeriodos.objects.get(rowid_per=rowid_per)
        per.estatus_per = "B"
    except SeCatPeriodos.DoesNotExist:
        raise Http404("El Periodo no existe")
    if request.POST: #Sobre escribe los valores
        messages.warning(request, "¡Periodo eliminado con exito!")
        per.save()
        return redirect('vista_periodos')
    return render(request, "controlEscolar/catalogos/universidad/GestionPeriodos/BorrarPeriodos.html", {"Periodos": per})
# Modifica un registro
@login_required
def vista_periodos_detail(request, rowid_per):
    per = SeCatPeriodos.objects.get(rowid_per=rowid_per)
    form = FormPeriodos(instance = per)
    if request.method == 'POST': #Sobre escribe los valores
        form = FormPeriodos(request.POST, instance = per)
        if form.is_valid():
            form.save()
            messages.info(request, "¡Periodo actualizado con exito!")
            return redirect('vista_periodos') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") # Emvia un mensaje para notificar que algun campo no es valido
            return render(request, "controlEscolar/catalogos/universidad/GestionPeriodos/ActualizarPeriodos.html", {"FormPeriodos" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/universidad/GestionPeriodos/ActualizarPeriodos.html", {"FormPeriodos" : form})#envia al detalle para actualizar
# Imprimir
class Export_print_periodos(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaPer = SeCatPeriodos.objects.filter(estatus_per="A") 
        data = {
            'count': listaPer.count(),
            'per': listaPer
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionPeriodos/listaPeriodos.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_periodos(LoginRequiredMixin,View):
    def get(self, request,*args, **kwargs):
        listaPer=SeCatPeriodos.objects.filter(estatus_per="A") 
        data = {
            'count': listaPer.count(),
            'per': listaPer
        }
        pdf = render_to_pdf('controlEscolar/catalogos/universidad/GestionPeriodos/listaPeriodos.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaPeriodos.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria 
@login_required
def export_csv_periodos (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaPeriodos.csv;'
    writer = csv.writer(response)
    writer.writerow(['Evento', 'Consecutivo', 'Fecha Inicial', 'Fecha Final','Año','Periodo','Descripcion'])
    listaPer=SeCatPeriodos.objects.filter(estatus_per="A") 
    for per in listaPer:
        writer.writerow([per.evento_per, per.consecutivo_per, per.fecha_inicial_per, per.fecha_final_per, per.anio_per, per.periodo_per, per.descripcion_per])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_periodos (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaPeriodos.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Periodos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Evento', 'Consecutivo', 'Fecha Inicial', 'Fecha Final','Año','Periodo','Descripcion']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatPeriodos.objects.filter(estatus_per="A").values_list('evento_per', 'consecutivo_per', 'fecha_inicial_per', 
                                                                'fecha_final_per', 'anio_per', 'periodo_per', 'descripcion_per')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

# -------------------------------------------- Plan de Estudios  --------------------------------------------- #

##############################################   PLAN DE ESTUDIOS    ##############################################
# #Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaPlanE(request):
    listaPlanE=SeCatPlaEstudio.objects.filter(estatus_plan_est="A").order_by('rowid_plan_est') #Lista de todos los planes de estudio que tengan el status = A  
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
            plan.rowid_plan_est = ultimo_id.rowid_plan_est + 1 # agrega uno al ultimo id insertado:
            form.save()
            messages.success(request, "¡Plan agregado con exito!") 
            return redirect('vista_Plan_Estudios')#redirecciona a la vista
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/GestionPE.html",{'entity' : listaPlanE, 'paginator' : paginator, 'FormsPlaE' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method =='GET':
        busqueda = request.GET.get("search_planE", None)
        print(busqueda)
        if busqueda:
            listaPlanE = SeCatPlaEstudio.objects.filter(
                #Revisión de los campos de la tabla en la BD
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
    return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/GestionPE.html",data)
# Update de estatus de 'A' a 'B' "ELIMINACION"
@login_required
def eliminarPlan(request, rowid_plan_est):
    try:
        plan = SeCatPlaEstudio.objects.get(rowid_plan_est=rowid_plan_est)
        plan.estatus_plan_est = "B"
    except SeCatPlaEstudio.DoesNotExist:
        raise Http404("El plan no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "¡Plan eliminado con exito!")
        plan.save()
        return redirect('vista_Plan_Estudios')
    return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/BorrarPE.html", {"Plan": plan})
# Modificar 
@login_required
def vista_planE_detail(request, rowid_plan_est):
    plan = SeCatPlaEstudio.objects.get(rowid_plan_est=rowid_plan_est)
    form = FormsPlaE(instance=plan)
    if request.method == 'POST': #Sobre escribe los valores
        form= FormsPlaE(request.POST, instance=plan) 
        plan.save() #Guarda cambios
        if form.is_valid():
            messages.info(request, "¡Plan actualizado con exito!")
            form.save()
            return redirect('vista_Plan_Estudios') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/ActualizarPE.html", {"FormsPlaE": form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/planEstudio/PlanEstudios/ActualizarPE.html", {"FormsPlaE": form})#envia al detalle para actualizar
# vista para imprimir pdf 
class Export_print_planE(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaPlan=SeCatPlaEstudio.objects.filter(estatus_plan_est="A") 
        data = {
            'count': listaPlan.count(),
            'planes': listaPlan
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/PlanEstudios/ListarPE.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#ESTA SI JALA COMO PDF NO LAS MAMADAS DE ARRIBA :D
class Export_pdf_planE(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaPlan=SeCatPlaEstudio.objects.filter(estatus_plan_est="A") 
        data = {
            'count': listaPlan.count(),
            'planes': listaPlan
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/PlanEstudios/ListarPE.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaPlanesEstudio.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises al formato  CSV 
@login_required
def export_csv_planE (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaPlanesEstudio.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Nombre', 'Abreviatura', 'Fecha de alta', 'Modificado por', 'Fecha de baja', 'Modificado por', 'Estatus'])
    listaPlanE=SeCatPlaEstudio.objects.filter(estatus_plan_est="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for plan in listaPlanE:
        writer.writerow([plan.id_plan_est, plan.decri_larga_plan_est, plan.descri_corta_plan_est,
                            plan.fec_alta_estpla, plan.user_alta_estpla, plan.fec_baja_estpla, plan.user_baja_estpla, plan.estatus_plan_est])
    return response
# Exportar paises a xlwt 
@login_required
def export_xlwt_plan (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaPlanesEstudio.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Plan')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Nombre', 'Abreviatura',  'Fecha de alta', 'Modificado', 'Fecha de baja', 'Modificado','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatPlaEstudio.objects.filter(estatus_plan_est="A").values_list('id_plan_est','decri_larga_plan_est', 'descri_corta_plan_est',
                                                                            'fec_alta_estpla', 'user_alta_estpla', 'fec_baja_estpla', 'user_baja_estpla', 'estatus_plan_est')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################################################  ASIGNATURA     ########################################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaAsi(request):
    listaAsignatura=SeCatAsignatura.objects.filter(estatus_asi="A").order_by('rowid_asignatura')#Lista de todos los paises que tengan el status = A
    contador_id = listaAsignatura.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaAsignatura, 9)
        listaAsignatura = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormsAsignatura(request.POST)
        if form.is_valid():
            asigna = form.save(commit=False)
            ultimo_id = SeCatAsignatura.objects.all().last()
            asigna.rowid_asignatura = ultimo_id.rowid_asignatura + 1
            asigna.save()
            messages.success(request, "¡La asignatura fue agregado con exito!")
            #redirecciona a la vista 
            return redirect('vista_asignatura')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/planEstudio/asignatura/GestionAsignatura.html",{'entity' : listaAsignatura,'paginator' : paginator, 'FormsAsignatura' : form,'contador' : contador_id,}) 
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_asi", None)
        print(busqueda)
        if busqueda:
            listaAsignatura = SeCatAsignatura.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(descri_larga_asi__icontains = busqueda),
                Q(estatus_asi__icontains = "A")
            ).distinct()
    form = FormsAsignatura()
    data = {
        'entity' : listaAsignatura,
        'paginator' : paginator,
        'FormsAsignatura' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/planEstudio/asignatura/GestionAsignatura.html",data)
##Eliminar
def eliminarAsignatura(request, rowid_asignatura):
    try:
        asi = SeCatAsignatura.objects.get(rowid_asignatura=rowid_asignatura)
        asi.estatus_asi = "B"
    except SeCatAsignatura.DoesNotExist:
        raise Http404("La asignatura no existe")
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "¡La asignatura fue eliminada con exito!")
        asi.save()
        return redirect('vista_asignatura')
    return render(request, "controlEscolar/catalogos/planEstudio/asignatura/BorrarAsignatura.html", {"Asi": asi})
#Modificar
def vista_asig_detail(request, rowid_asignatura):
    asi = SeCatAsignatura.objects.get(rowid_asignatura=rowid_asignatura)
    form = FormsAsignatura(instance=asi)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormsAsignatura(request.POST, instance=asi)
        if form.is_valid():
            messages.info(request, "Asignatura actualizada")
            form.save() #Guarda cambios
            return redirect('vista_asignatura') #retorna despues de actualizar CAMBIAR RETORNO
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/planEstudio/asignatura/ActualizarAsignatura.html", {"FormsAsignatura" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/planEstudio/asignatura/ActualizarAsignatura.html", {"FormsAsignatura" : form})#envia al detalle para actualizar
# vista para "PRINT"
class Export_print_asi(View):
    def get(self, request, *args, **kwargs):
        listaAsi=SeCatAsignatura.objects.filter(estatus_asi="A") 
        data = {
            'count': listaAsi.count(),
            'planes': listaAsi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/asignatura/ListarAsignatura.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#PDF
class Export_pdf_asi(View):
    def get(self, request,*args, **kwargs):
        listaAsi=SeCatAsignatura.objects.filter(estatus_asi="A") 
        data = {
            'count': listaAsi.count(),
            'planes': listaAsi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/asignatura/ListarAsignatura.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaAsignaturas.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises al formato  CSV 
def export_csv_asi (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaAsignaturas.csv;'
    writer = csv.writer(response)
    writer.writerow(['Plan de estudio', 'Carrera', 'Id Asignatura', 'Nombre', 'Abreviatura', 'Estatus'])
    listaAsi=SeCatAsignatura.objects.filter(estatus_asi="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for asi in listaAsi:
        writer.writerow([asi.rowid_plan_est, asi.rowid_car, asi.id_asignatura, asi.descri_larga_asi, asi.descri_corto_asi, asi.estatus_asi])
    return response
# Exportar paises a xlwt 
def export_xlwt_asi (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaAsignatura.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicador')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Plan de estudio', 'Carrera', 'Id Asignatura', 'Nombre', 'Abreviatura', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatAsignatura.objects.filter(estatus_asi="A").values_list('rowid_plan_est', 'rowid_car', 'id_asignatura', 'descri_larga_asi', 'descri_corto_asi', 'estatus_asi')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

########################################################### Indicadores ###########################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaIndicador(request):
    #Lista de todos los paises que tengan el status = A
    listaIndicador=SeCatIndicador.objects.filter(estatus_ind="A").order_by('rowid_indicador')
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
            indi.rowid_indicador = ultimo_id.rowid_indicador + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "¡El indicador fue agregado con exito!")
            return redirect('Vista_indicadores') #redirecciona a la vista 
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/GestionIndicadores.html",{'entity' : listaIndicador, 'paginator' : paginator, 'FormsIndicador' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_indicador", None)
        print(busqueda)
        if busqueda:
            listaIndicador = SeCatIndicador.objects.filter(
                #Revisión de los campos de la tabla en la BD
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
@login_required
def eliminarIndicador(request, rowid_indicador):
    try:
        indi = SeCatIndicador.objects.get(rowid_indicador=rowid_indicador)
        indi.estatus_ind = "B"
    except SeCatIndicador.DoesNotExist:
        raise Http404("El indicador no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "¡Indicador eliminado con exito!")
        indi.save()
        return redirect('Vista_indicadores')
    return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/BorrarIndicadores.html", {"Indi": indi})
###modificar
@login_required
def vista_indicador_detail(request, rowid_indicador):
    indi = SeCatIndicador.objects.get(rowid_indicador=rowid_indicador)
    form = FormsIndicador(instance=indi)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormsIndicador(request.POST, instance=indi)
        if form.is_valid():
            indi.save() #Guarda cambios
            messages.info(request, "¡Indicador actualizado con exito!")
            return redirect('Vista_indicadores') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/ActualizarIndicadores.html", {"FormsIndicador" : form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/planEstudio/Indicadores/ActualizarIndicadores.html", {"FormsIndicador" : form})#envia al detalle para actualizar
# vista para "PRINT"
class Export_print_ind(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaIndi=SeCatIndicador.objects.filter(estatus_ind="A") 
        data = {
            'count': listaIndi.count(),
            'indicadores': listaIndi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/Indicadores/ListarIndicadores.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#PDF
class Export_pdf_indi(LoginRequiredMixin, View):
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
@login_required
def export_csv_indi (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaIndicadores.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Nombre', 'Abreviatura', 'Clave de control', 'Estatus'])
    listaIndi=SeCatIndicador.objects.filter(estatus_ind="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for indi in listaIndi:
        writer.writerow([indi.id_indicador, indi.descri_largo_ind, indi.descri_corto_ind, indi.cve_control_ind, indi.estatus_ind])
    return response
# Exportar paises a xlwt 
@login_required
def export_xlwt_indicador (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaIndicador.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicador')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id', 'Nombre', 'Abreviatura', 'Clave de control', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatIndicador.objects.filter(estatus_ind="A").values_list('id_indicador','descri_largo_ind', 'descri_corto_ind', 'cve_control_ind', 'estatus_ind')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

########################################################### Plan de estudios asignaturas  ###########################################

#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaPea(request):
    #Lista de todos los paises que tengan el status = A
    listaPea=SeProPlanEstudio.objects.filter(estatus_pea="A").order_by('rowid_pro_plan_est')
    contador_id = listaPea.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaPea, 9)
        listaPea = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormsPeA(request.POST)
        if form.is_valid():
            asigna = form.save(commit=False)
            ultimo_id = SeProPlanEstudio.objects.all().last()
            asigna.rowid_pro_plan_est = ultimo_id.rowid_pro_plan_est + 1
            asigna.save()
            messages.success(request, "¡La asignatura fue agregado con exito!")
            #redirecciona a la vista 
            return redirect('vista_pea')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/planEstudio/Pea/GestionPea.html",{'entity' : listaPea,'paginator' : paginator, 'FormsPeA' : form,'contador' : contador_id,}) 
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_asi", None)
        print(busqueda)
        if busqueda:
            listaPea = SeProPlanEstudio.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(horas_plan_est__icontains = busqueda),
                Q(estatus_pea__icontains = "A")
            ).distinct()
    form = FormsPeA()
    data = {
        'entity' : listaPea,
        'paginator' : paginator,
        'FormsPeA' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/planEstudio/Pea/GestionPea.html",data)
##Eliminar
def eliminarPea(request, rowid_pro_plan_est):
    try:
        asi = SeProPlanEstudio.objects.get(rowid_pro_plan_est=rowid_pro_plan_est)
        asi.estatus_pea = "B"
    except SeProPlanEstudio.DoesNotExist:
        raise Http404("La asignatura no existe")
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "¡La asignatura fue eliminada con exito!")
        asi.save()
        return redirect('vista_pea')
    return render(request, "controlEscolar/catalogos/planEstudio/Pea/BorrarPea.html", {"Asi": asi})
##Mod
def vista_pea_detail(request, rowid_pro_plan_est):
    asi = SeProPlanEstudio.objects.get(rowid_pro_plan_est=rowid_pro_plan_est)
    form = FormsPeA(instance=asi)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormsPeA(request.POST, instance=asi)
        if form.is_valid():
            messages.info(request, "Asignatura actualizada")
            form.save() #Guarda cambios
            return redirect('vista_pea') #retorna despues de actualizar CAMBIAR RETORNO
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/planEstudio/Pea/ActualizarPea.html", {"FormsPeA" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/planEstudio/Pea/ActualizarPea.html", {"FormsPeA" : form})#envia al detalle para actualizar
# vista para "PRINT"
class Export_print_pea(View):
    def get(self, request, *args, **kwargs):
        listaPea=SeProPlanEstudio.objects.filter(estatus_pea="A") 
        data = {
            'count': listaPea.count(),
            'planes': listaPea
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/Pea/ListarPea.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#PDF
class Export_pdf_pea(View):
    def get(self, request,*args, **kwargs):
        listaPea=SeProPlanEstudio.objects.filter(estatus_pea="A") 
        data = {
            'count': listaPea.count(),
            'planes': listaPea
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/Pea/ListarPea.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'listaPlanEstudiosAsignatura.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises al formato  CSV 
def export_csv_pea (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaAsignaturas.csv;'
    writer = csv.writer(response)
    writer.writerow(['Asignatura',' Plan', 'Grado', 'Carrera', 'Total de horas', 'Creditos', 'Nota minima','Valor', 'Estatus'])
    listaAsi=SeProPlanEstudio.objects.filter(estatus_pea="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for asi in listaAsi:
        writer.writerow([asi.rowid_asignatura, asi.rowid_plan_est, asi.rowid_grado, asi.rowid_car, asi.horas_plan_est, asi.creditos_plan_est ,asi.nota_minima_apro_est, asi.valor_pon_final, asi.estatus_pea])
    return response
# Exportar paises a xlwt 
def export_xlwt_pea (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaAsignatura.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicador')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Asignatura',' Plan', 'Grado', 'Carrera', 'Total de horas', 'Creditos', 'Nota minima','Valor', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeProPlanEstudio.objects.filter(estatus_pea="A").values_list('rowid_asignatura', 'rowid_plan_est', 'rowid_grado', 'rowid_car', 'horas_plan_est', 'creditos_plan_est', 'nota_minima_apro_est', 'valor_pon_final', 'estatus_pea')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

########################################################### Plan de estudios asignatura indicador   ###########################################

@login_required
def vistaPlanEAI(request):
    #Lista de todos los paises que tengan el status = A
    listaPea=SeProAsiIndicador.objects.filter(estatus_peai="A").order_by('rowid_pro_asi_ind')
    contador_id = listaPea.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaPea, 9)
        listaPea = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormsPeaI(request.POST)
        if form.is_valid():
            asigna = form.save(commit=False)
            ultimo_id = SeProAsiIndicador.objects.all().last()
            asigna.rowid_pro_asi_ind = ultimo_id.rowid_pro_asi_ind + 1
            asigna.save()
            messages.success(request, "¡La asignatura Indicador fue agregado con exito!")
            #redirecciona a la vista 
            return redirect('vista_planEAI')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/planEstudio/Peai/GestionPeai.html",{'entity' : listaPea,'paginator' : paginator, 'FormsPeaI' : form,'contador' : contador_id,}) 
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_asigna", None)
        print(busqueda)
        if busqueda:
            listaPea = SeProAsiIndicador.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(porcentaje_pro_asi_idi__icontains = busqueda),
                Q(estatus_peai__icontains = "A")
            ).distinct()
    form = FormsPeaI()
    data = {
        'entity' : listaPea,
        'paginator' : paginator,
        'FormsPeaI' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/planEstudio/Peai/GestionPeai.html",data)
##Eliminar
@login_required
def eliminarPeai(request, rowid_pro_asi_ind):
    try:
        peai = SeProAsiIndicador.objects.get(rowid_pro_asi_ind=rowid_pro_asi_ind)
        peai.estatus_peai = "B"
    except SeProAsiIndicador.DoesNotExist:
        raise Http404("El plan no existe")
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "Plan eliminado con exito!")
        peai.save()
        return redirect('vista_planEAI')
    return render(request, "controlEscolar/catalogos/planEstudio/Peai/BorrarPeai.html", {"Plan": peai})
# Modifica un registro
@login_required
def vista_peai_detail(request, rowid_pro_asi_ind):
    peai = SeProAsiIndicador.objects.get(rowid_pro_asi_ind=rowid_pro_asi_ind)
    form = FormsPeaI(instance = peai)
    if request.POST: #Sobre escribe los valores
        form = FormsPeaI(request.POST, instance = peai)
        if form.is_valid():
            messages.info(request, "¡Plan actualizado con exito!")
            form.save()
            return redirect('vista_planEAI') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/planEstudio/Peai/ActualizarPeai.html", {"FormsPeaI" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/planEstudio/Peai/ActualizarPeai.html", {"FormsPeaI" : form})#envia al detalle para actualizar
# vista para "PRINT"
class Export_print_peai(View):
    def get(self, request, *args, **kwargs):
        listaPeai=SeProAsiIndicador.objects.filter(estatus_peai="A") 
        data = {
            'count': listaPeai.count(),
            'planes': listaPeai
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/Peai/ListarPeai.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#PDF
class Export_pdf_peai(View):
    def get(self, request,*args, **kwargs):
        listaPeai=SeProAsiIndicador.objects.filter(estatus_peai="A") 
        data = {
            'count': listaPeai.count(),
            'planes': listaPeai
        }
        pdf = render_to_pdf('controlEscolar/catalogos/planEstudio/Peai/ListarPeai.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'listaPlanEstudiosAsignaturaIndicador.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises al formato  CSV 
def export_csv_peai (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaPlanEstudioAsignaturaIndicador.csv;'
    writer = csv.writer(response)
    writer.writerow(['Plan de estudios','Indicador', 'Porcentaje', 'Comentario', 'Estatus'])
    listaAsi=SeProAsiIndicador.objects.filter(estatus_peai="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for asi in listaAsi:
        writer.writerow([asi.rowid_pro_plan_est, asi.rowid_indicador, asi.porcentaje_pro_asi_idi, asi.comen_pro_asi_ind, asi.estatus_peai ])
    return response
# Exportar paises a xlwt 
def export_xlwt_peai (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaPlanEstudioAsignaturaIndicador.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicador')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Plan de estudios','Indicador', 'Porcentaje', 'Comentario', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeProAsiIndicador.objects.filter(estatus_peai="A").values_list('rowid_pro_plan_est', 'rowid_indicador', 'porcentaje_pro_asi_idi', 'comen_pro_asi_ind', 'estatus_peai')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

# -------------------------------------------- Aspirantes --------------------------------------------- #

##############################################   Escuela de Procedencia   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaEscProc(request):
    listaEscProc = SeCatEscuelaProcedencia.objects.filter(estatus_esc_proc="A").order_by('rowid_esc_proc')
    contador_id = listaEscProc.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaEscProc, 7)
        listaEscProc = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormEscProc(request.POST)
        if form.is_valid():
            escpro = form.save(commit=False)
            ultimo_id = SeCatEscuelaProcedencia.objects.all().order_by('rowid_esc_proc').last()
            escpro.rowid_esc_proc = ultimo_id.rowid_esc_proc + 1
            escpro.save()
            messages.success(request, "¡Escuela agregada con exito!")
            return redirect('vista_escpro')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionEscuelaProc/GestionEscuelaProc.html",{'entity' : listaEscProc,'paginator' : paginator,'FormEscProc' : form,'contador': contador_id})
    elif request.method == 'GET':
        busqueda = request.GET.get("search_escpro", None)
        if busqueda:
            listaEscProc = SeCatEscuelaProcedencia.objects.filter(
                Q(nombre_esc_proc__icontains = busqueda),
                Q(estatus_esc_proc__icontains = "A")
            ).distinct()
    form = FormEscProc()
    data = {
        'entity' : listaEscProc,
        'paginator' : paginator,
        'FormEscProc' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/aspirantes/GestionEscuelaProc/GestionEscuelaProc.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarEscProc(request, rowid_esc_proc):
    try:
        escpro = SeCatEscuelaProcedencia.objects.get(rowid_esc_proc = rowid_esc_proc)
        escpro.estatus_esc_proc = "B"
    except SeCatEscuelaProcedencia.DoesNotExist:
        raise Http404("La Escuela no existe")
    if request.method == 'POST': #Sobre escrive los valores
        escpro.save()
        messages.warning(request, "¡Escuela eliminado con exito!")
        return redirect('vista_escpro')
    return render(request, "controlEscolar/catalogos/aspirantes/GestionEscuelaProc/BorrarEscuelaProc.html", {"EscPro": escpro})
# Modifica un registro
@login_required
def vista_escpro_detail(request, rowid_esc_proc):
    escpro = SeCatEscuelaProcedencia.objects.get(rowid_esc_proc = rowid_esc_proc)
    form = FormEscProc(instance=escpro)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormEscProc(request.POST, instance = escpro)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "¡Escuela actualizada con exito!")
            return redirect('vista_escpro') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionEscuelaProc/ActualizarEscuelaProc.html", {"FormEscProc" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/aspirantes/GestionEscuelaProc/ActualizarEscuelaProc.html", {"FormEscProc" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_escpro(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaEscProc = SeCatEscuelaProcedencia.objects.filter(estatus_esc_proc="A")
        data = {
            'count': listaEscProc.count(),
            'escpro': listaEscProc
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionEscuelaProc/ListaEscuelaProc.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_escpro(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaEscProc = SeCatEscuelaProcedencia.objects.filter(estatus_esc_proc="A")
        data = {
            'count': listaEscProc.count(),
            'escpro': listaEscProc
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionEscuelaProc/ListaEscuelaProc.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Lista Escuelas.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria
@login_required
def export_csv_escpro (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=Lista Escuelas.csv;'
    writer = csv.writer(response)
    writer.writerow(['Municipio', 'CCT','Nombre de la escuela', 'Tipo de Escuela', 'Servicio','Estatus'])
    listaEscProc = SeCatEscuelaProcedencia.objects.filter(estatus_esc_proc="A")
    for ep in listaEscProc:
        writer.writerow([ep.rowid_mundel, ep.cct_esc_proc, ep.nombre_esc_proc, ep.control_esc_proc, ep.servicio_esc_proc, ep.estatus_esc_proc])
    return response
# Exportar paises a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_escpro (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=Lista Escuelas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Escuelas de Procedencia')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Municipio','CCT','Nombre de la Escuela', 'Tipo de Escuela', 'Servicio', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatEscuelaProcedencia.objects.filter(estatus_esc_proc="A").values_list('rowid_mundel', 'cct_esc_proc','nombre_esc_proc', 'control_esc_proc','servicio_esc_proc','estatus_esc_proc')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################   MEDIOS DE DIFUSION  #######################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_Medios(request):
    listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A").order_by('rowid_medio_dif')
    contador_id = listaMedios.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaMedios, 9)
        listaMedios = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormMediosDifusion(request.POST)
        if form.is_valid():
            medio = form.save(commit=False)
            ultimo_id = SeCatMedioDifusion.objects.all().order_by('rowid_medio_dif').last() 
            medio.rowid_medio_dif = ultimo_id.rowid_medio_dif + 1 
            medio.save()
            messages.success(request, "¡Medio de Difusión agregado con exito!")
            return redirect('vista_Medios') 
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/GestionMD.html",{'entity' : listaMedios, 'paginator' : paginator, 'FormMediosDifusion' : form, 'contador': contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_medios", None)
        print(busqueda)
        if busqueda:
            listaMedios = SeCatMedioDifusion.objects.filter(
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
@login_required
def eliminar_Medio(request, rowid_medio_dif):
    try:
        medio = SeCatMedioDifusion.objects.get(rowid_medio_dif=rowid_medio_dif)
        medio.estatus_dif = "B"
    except SeCatMedioDifusion.DoesNotExist:
        raise Http404("El Medio de Difusión no existe")
    if request.method == 'POST':
        medio.save()
        messages.warning(request, "¡Medio de Difusión eliminado con exito!")
        return redirect('vista_Medios')
    return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/BorrarMD.html", {"Medio": medio})
# Modifica un registro
@login_required
def vista_medios_detail(request, rowid_medio_dif):
    medio = SeCatMedioDifusion.objects.get(rowid_medio_dif=rowid_medio_dif)
    form = FormMediosDifusion(instance=medio)
    if request.method == 'POST':
        form = FormMediosDifusion(request.POST, instance = medio)
        if form.is_valid():
            medio = form.save(commit=False)
            medio.save()
            messages.info(request, "¡Medio de Difusión actualizado con exito!")
            return redirect('vista_Medios')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/ActualizarMD.html", {"FormMediosDifusion" : form})
    return render(request, "controlEscolar/catalogos/aspirantes/GestionMediosDifusion/ActualizarMD.html", {"FormMediosDifusion" : form})
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_medios(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A") 
        data = {
            'count': listaMedios.count(),
            'medios': listaMedios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionMediosDifusion/listaMD.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_medios(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A") 
        data = {
            'count': listaMedios.count(),
            'medios': listaMedios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionMediosDifusion/listaMD.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaMediosdeDifusión.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_medios (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaMediosdeDifusión.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave Medio de Difusión', 'Medio de Difusión', 'Abreviatura', 'Estatus'])
    listaMedios=SeCatMedioDifusion.objects.filter(estatus_dif="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for medio in listaMedios:
        writer.writerow([medio.id_medio_dif, medio.descri_largo_meddif, medio.descri_corto_meddif, medio.estatus_dif])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_medios (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaMediosdeDifusión.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Medios')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave Medio de Difusión', 'Medio de Difusión', 'Abreviatura', 'Estatus']
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

###################################################   Tipo de Escuelas  ###########################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_Escuelas(request):
    listaEscuelas=SeCatTipoEscuela.objects.filter(estatus_esc="A").order_by('rowid_tipo_esc')
    contador_id = listaEscuelas.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaEscuelas, 9)
        listaEscuelas = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormTiposEscuelas(request.POST)
        if form.is_valid():
            escuela = form.save(commit=False)
            ultimo_id = SeCatTipoEscuela.objects.all().order_by('rowid_tipo_esc').last() 
            escuela.rowid_tipo_esc = ultimo_id.rowid_tipo_esc + 1
            escuela.save()
            messages.success(request, "¡Escuela agregada con exito!")
            return redirect('vista_Escuelas')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/GestionEscuelas.html",{'entity':listaEscuelas, 'paginator':paginator, 'FormTiposEscuelas':form, 'contador':contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_escuelas", None)
        print(busqueda)
        if busqueda:
            listaEscuelas = SeCatTipoEscuela.objects.filter(
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
@login_required
def eliminar_Escuela(request, rowid_tipo_esc):
    try:
        escuela = SeCatTipoEscuela.objects.get(rowid_tipo_esc=rowid_tipo_esc)
        escuela.estatus_esc = "B"
    except SeCatTipoEscuela.DoesNotExist:
        raise Http404("La Escuela no existe")
    if request.method == 'POST':
        escuela.save()
        messages.warning(request, "¡Escuela eliminada con exito!")
        return redirect('vista_Escuelas')
    return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/BorrarEscuela.html", {"Escuela": escuela})
# Modifica un registro
@login_required
def vista_escuelas_detail(request, rowid_tipo_esc):
    escuela = SeCatTipoEscuela.objects.get(rowid_tipo_esc=rowid_tipo_esc)
    form = FormTiposEscuelas(instance=escuela)
    if request.method == 'POST':
        form = FormTiposEscuelas(request.POST, instance = escuela)
        if form.is_valid():
            escuela = form.save(commit=False)
            escuela.save()
            messages.info(request, "¡Escuela actualizada con exito!")
            return redirect('vista_Escuelas')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/ActualizarEscuela.html", {"FormTiposEscuelas" : form})
    return render(request, "controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/ActualizarEscuela.html", {"FormTiposEscuelas" : form})
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_escuelas(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaEscuelas=SeCatTipoEscuela.objects.filter(estatus_esc="A") 
        data = {
            'count': listaEscuelas.count(),
            'escuelas': listaEscuelas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionTiposEscuelas/listaEscuelas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_escuelas(LoginRequiredMixin, View):
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
@login_required
def export_csv_escuelas (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposdeEscuelas.csv;'
    writer = csv.writer(response)
    writer.writerow(['Id Colonia','Clave Tipo de Escuela','Nombre Tipo de Escuela','Abreviatura','Nombre Institución','Nombre Plantel','Estatus'])
    listaEscuelas=SeCatTipoEscuela.objects.filter(estatus_esc="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for esc in listaEscuelas:
        writer.writerow([esc.rowid_col,esc.id_tipo_esc,esc.descri_largo_esc,esc.descri_corta_esc,esc.institucion,esc.nombre_plantel,esc.estatus_esc])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_escuelas (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposdeEscuelas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Escuelas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Id Colonia','Clave Tipo de Escuela','Nombre Tipo de Escuela','Abreviatura','Nombre Institución','Nombre Plantel','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatTipoEscuela.objects.filter(estatus_esc="A").values_list('rowid_col','id_tipo_esc','descri_largo_esc','descri_corta_esc','institucion','nombre_plantel','estatus_esc')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################  Areas Bachillerato  ###############################################
#Agregar si es post y lista de todos / Aqui va la paginación
@login_required
def vista_AreaBachi(request):
    listaAreaBachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A").order_by('rowid_area_bac')
    contador_id = listaAreaBachi.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaAreaBachi, 9)
        listaAreaBachi = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormAreaBachi(request.POST)
        if form.is_valid():
            areabachi = form.save(commit=False)
            ultimo_id = SeCatAreaBachillerato.objects.all().order_by('rowid_area_bac').last() 
            areabachi.rowid_area_bac = ultimo_id.rowid_area_bac + 1
            areabachi.save()
            messages.success(request, "¡Área bachillerato agregado con exito!")
            return redirect('vista_AreaBachi')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionAreaBachi/GestionAreaBachi.html",{'entity' : listaAreaBachi, 'paginator' : paginator, 'FormAreaBachi' : form, 'contador' : contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_areabachillerato", None)
        if busqueda:
            listaAreaBachi = SeCatAreaBachillerato.objects.filter(
                Q(descri_larga_bac__icontains = busqueda),
                Q(estatus_bac__icontains = "A")
            ).distinct()
    form = FormAreaBachi()
    data = {
        'entity' : listaAreaBachi,
        'paginator' : paginator,
        'FormAreaBachi' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/aspirantes/GestionAreaBachi/GestionAreaBachi.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminar_AreaBachi(request, rowid_area_bac):
    try:
        areabachi = SeCatAreaBachillerato.objects.get(rowid_area_bac=rowid_area_bac)
        areabachi.estatus_bac = "B"
    except SeCatAreaBachillerato.DoesNotExist:
        raise Http404("Área Bachillerato no existe")
    if request.method == 'POST':
        areabachi.save()
        messages.warning(request, "¡Área Bachillerato eliminada con exito!")
        return redirect('vista_AreaBachi')
    return render(request, "controlEscolar/catalogos/aspirantes/GestionAreaBachi/BorrarAreaBachi.html", {"AreaBachi":areabachi})
# Modifica un registro
@login_required
def vista_AreaBachi_detail(request, rowid_area_bac):
    areabachi = SeCatAreaBachillerato.objects.get(rowid_area_bac = rowid_area_bac)
    form = FormAreaBachi(instance = areabachi)
    if request.method == 'POST':
        form = FormAreaBachi(request.POST, instance = areabachi)
        if form.is_valid():
            areabachi = form.save(commit=False)
            areabachi.save()
            messages.info(request, "¡Área Bachillerato actualizada con exito!")
            return redirect('vista_AreaBachi')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionAreaBachi/ActualizarAreaBachi.html", {"FormAreaBachi" : form})
    return render(request, "controlEscolar/catalogos/aspirantes/GestionAreaBachi/ActualizarAreaBachi.html", {"FormAreaBachi" : form})
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_areabachi(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        areabachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A") 
        data = {
            'count': areabachi.count(),
            'areabachi': areabachi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionAreaBachi/ListaAreaBachi.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_areabachi(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        areabachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A") 
        data = {
            'count': areabachi.count(),
            'areabachi': areabachi
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionAreaBachi/ListaAreaBachi.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaÁreaBachillerato.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_areabachi (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaÁreaBachillerato.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave Área Bachillerato', 'Nombre Área Bachillerato', 'Abreviatura', 'Estatus'])
    areabachi=SeCatAreaBachillerato.objects.filter(estatus_bac="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for areabac in areabachi:
        writer.writerow([areabac.id_area_bac, areabac.descri_larga_bac, areabac.descri_corta_bac, areabac.estatus_bac])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_areabachi (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaÁreaBachillerato.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Area Bac')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave Área Bachillerato', 'Nombre Área Bachillerato', 'Abreviatura', 'Estatus']
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

##############################################  INDICADORES ASPIRANTES  ####################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_IndAsp(request):
    listaIndAsp = SeProIndAsp.objects.filter(estatus_indicadores="A").order_by('rowid_pro_ind_asp')
    contador_id = listaIndAsp.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaIndAsp, 9)
        listaIndAsp = paginator.page(page)
    except:
        raise Http404 
    if request.method == 'POST':
        form = FormIndAsp(request.POST)
        if form.is_valid():
            IndAsp = form.save(commit=False)
            ultimo_id = SeProIndAsp.objects.all().order_by('rowid_pro_ind_asp').last()
            IndAsp.rowid_pro_ind_asp = ultimo_id.rowid_pro_ind_asp + 1
            IndAsp.save()
            messages.success(request, "¡Indicador Aspirante agregado con exito!")
            return redirect('vista_IndAsp')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionIndAsp/GestionIndAsp.html",{'entity' : listaIndAsp, 'paginator' : paginator,'FormIndAsp' : form, 'contador': contador_id,})       
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_IndAsp", None)
        print(busqueda)
        if busqueda:
            listaIndAsp = SeProIndAsp.objects.filter(
                Q(valor_porcentual__icontains = busqueda),
                Q(estatus_indicadores__icontains = "A")
            ).distinct()
    form = FormIndAsp()
    data = {
        'entity' : listaIndAsp,
        'paginator' : paginator,
        'FormIndAsp' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/aspirantes/GestionIndAsp/GestionIndAsp.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminar_IndAsp(request, rowid_pro_ind_asp):
    try:
        IndAsp = SeProIndAsp.objects.get(rowid_pro_ind_asp=rowid_pro_ind_asp)
        IndAsp.estatus_indicadores = "B"
    except SeProIndAsp.DoesNotExist:
        raise Http404("El Indicador Aspirante no existe")
    if request.method == 'POST':
        IndAsp.save()
        messages.warning(request, "¡Indicador Aspirante eliminado con exito!")
        return redirect('vista_IndAsp')
    return render(request, "controlEscolar/catalogos/aspirantes/GestionIndAsp/BorrarIndAsp.html", {"IndAsp": IndAsp})
# Modifica un registro
@login_required
def vista_IndAsp_detail(request, rowid_pro_ind_asp):
    IndAsp = SeProIndAsp.objects.get(rowid_pro_ind_asp=rowid_pro_ind_asp)
    form = FormIndAsp(instance = IndAsp)
    if request.method == 'POST':
        form = FormIndAsp(request.POST, instance = IndAsp)
        if form.is_valid():
            IndAsp = form.save(commit=False)
            IndAsp.save()
            messages.info(request, "¡Indicador Aspirante actualizado con exito!")
            return redirect('vista_IndAsp')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/aspirantes/GestionIndAsp/ActualizarIndAsp.html", {"FormIndAsp" : form})
    return render(request, "controlEscolar/catalogos/aspirantes/GestionIndAsp/ActualizarIndAsp.html", {"FormIndAsp" : form})
# primera de pdf posible imprimir 
class Export_print_IndAsp(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaIndAsp = SeProIndAsp.objects.filter(estatus_indicadores="A")
        data = {
            'count': listaIndAsp.count(),
            'IndAsp': listaIndAsp
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionIndAsp/ListaIndAsp.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Divisiones
class Export_pdf_IndAsp(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaIndAsp=SeProIndAsp.objects.filter(estatus_indicadores="A")
        data = {
            'count': listaIndAsp.count(),
            'IndAsp': listaIndAsp
        }
        pdf = render_to_pdf('controlEscolar/catalogos/aspirantes/GestionIndAsp/ListaIndAsp.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaIndicadoresAspirantes.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria
@login_required
def export_csv_IndAsp (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaIndicadoresAspirantes.csv;'
    writer = csv.writer(response)
    writer.writerow(['Carrera','Indicador','Clave Indicador-Aspirante','Valor Porcentual','Estatus'])
    listaIndAsp=SeProIndAsp.objects.filter(estatus_indicadores="A")
    for Ind in listaIndAsp:
        writer.writerow([Ind.rowid_car, Ind.rowid_indicador ,Ind.rowid_pro_ind_asp ,Ind.valor_porcentual ,Ind.estatus_indicadores])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_IndAsp (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaIndicadoresAspirantes.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicadores-Aspirantes')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Carrera','Indicador','Clave Indicador-Aspirante','Valor Porcentual','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeProIndAsp.objects.filter(estatus_indicadores="A").values_list('rowid_car','rowid_indicador','rowid_pro_ind_asp','valor_porcentual','estatus_indicadores')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

# -------------------------------------------- Estudiantes --------------------------------------------- #

######################################### Estudiante ##############################################
@login_required
def vistaEstudiante(request):
    #Lista de todos los planes de estudio que tengan el status = A
    listaEstudiante=SeTabEstudiante.objects.filter(estatus_est="A").order_by('rowid_matricula')
    contador_id = listaEstudiante.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaEstudiante, 6)
        listaEstudiante = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST': #Valida que sea una peticion de tipo post / Guarda datos
        form = FormsEstudiante(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            ultimo_id = SeTabEstudiante.objects.all().last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id
            doc.rowid_matricula =  ultimo_id.rowid_matricula + 1 # agrega uno al ultimo id insertado:
            form.save()
            messages.success(request, "¡Estudiante agregado con exito!")
            return redirect('vista_estudiante')#redirecciona a la vista
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/estudiante/GestionEstudiante.html",{'entity' : listaEstudiante, 'paginator' : paginator, 'FormsEstudiante' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method =='GET':
        busqueda = request.GET.get("search_estudiante", None)
        print(busqueda)
        if busqueda:
            listaEstudiante = SeTabEstudiante.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(nombre_estu__icontains = busqueda),
                Q(estatus_est__icontains = "A")
            ).distinct()
    form = FormsEstudiante()
    data = {
        'entity' : listaEstudiante,
        'paginator' : paginator,
        'FormsEstudiante' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/estudiante/GestionEstudiante.html",data)
#ELIMINAR
@login_required
def eliminarEstudiante(request, rowid_matricula):
    try:
        est = SeTabEstudiante.objects.get(rowid_matricula=rowid_matricula)
        est.estatus_est = "B"
    except SeTabEstudiante.DoesNotExist:
        raise Http404("El estudiante no existe")
    if request.POST: #Sobre escrive los valores
        messages.warning(request, "¡Estudiante eliminado con exito!")
        est.save()
        return redirect('vista_estudiante')
    return render(request, "controlEscolar/catalogos/estudiantes/estudiante/BorrarEstudiante.html", {"Est": est})
# Modificar
@login_required
def vista_estudiante_detail(request, rowid_matricula):
    est = SeTabEstudiante.objects.get(rowid_matricula=rowid_matricula)
    form = FormsEstudiante(instance=est)
    if request.method == 'POST': #Sobre escribe los valores
        form= FormsEstudiante(request.POST, instance=est)
        if form.is_valid():
            est.save() #Guarda cambios
            messages.info(request, "¡Estudiante actualizado con exito!")
            return redirect('vista_estudiante') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/estudiante/ActualizarEstudiante.html", {"FormsEstudiante": form})
    return render(request, "controlEscolar/catalogos/estudiantes/estudiante/ActualizarEstudiante.html", {"FormsEstudiante": form})
#print
class Export_print_estudiante(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaEstudiante=SeTabEstudiante.objects.filter(estatus_est="A")
        data = {
            'count': listaEstudiante.count(),
            'est': listaEstudiante
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/estudiante/ListarEstudiante.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
##PDF
class Export_pdf_estudiante(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaEstudiante=SeTabEstudiante.objects.filter(estatus_est="A")
        data = {
            'count': listaEstudiante.count(),
            'est': listaEstudiante
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/estudiante/ListarEstudiante.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaEstudiante.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a  csv
@login_required
def export_csv_estudiante (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaEstudiante.csv;'
    writer = csv.writer(response)
    writer.writerow(['Becas', 'Carrera', 'Colonia','Municipio','Escuela de Procedencia', 'Grupo','Id Estado', 'Matricula', 'Nombre(s)', 'Apellido paterno', 'Apelido materno', 'RFC', 'CURP','Direccion', 'Telefono', 'Correo electronico', 'Sexo','Fecha de alta', 'Usuario que dio alta', 'Fecha de baja', 'Usuario que dio de baja', 'Codigo postal','Fecha de nacimiento','Turno','Generacion','Periodo', 'Año de ingreso', 'Estado civil',  'Apellido materno del tutor', 'Apellido paterno del tutor', 'Folio del estudiante', 'Trabajo del estudiante', 'Tipo de sangre', 'Tipo de escuela', 'Área del bachillerato', 'Fecha de inicio del bachillerato', 'Fecha de fin del bachillerato', 'Promedio general del bachillerato', 'Telefono del trabajo', 'Edad del estudiante',  'Fecha de vigencia', 'Estatus de inscrito al Imms', 'Imss', 'Clinica', 'Numero de servicio', 'Fecha del servicio social','Fecha ', 'Matricula provicional',  'Beca de aprovechamiento', 'Usuario', 'Contraseña', 'Estatus de biblioteca', 'Tipo de carrera', 'Otras', 'Cedula del TSU', 'Referencia', 'Grasc', 'Institucion del seguro', 'Otras Op','Nacionalidad', 'Discapacidad', 'Tipo de discapacidad',  'Folio certificado', 'Fecha',  'Equivalencia',  'Parentesco tutor','Tipo de estudiante', 'Num exterior', 'Numero interior', 'Estatus'])
    listaEstudiante=SeTabEstudiante.objects.filter(estatus_est="A")
    for est in listaEstudiante:
        writer.writerow([est.rowid_becas, est.rowid_car, est.rowid_col,est.rowid_mundel, est.rowid_esc_proc, est.rowid_grupo, est.id_matricula, est.nombre_estu, est.paterno_est, est.materno_est, est.rfc_est, est.curp_est, est.direccion_est, est.telefono_est,  est.email_est, est.sexo_est, est.fecha_alta_est, est.user_alta_est, est.fecha_cambio_est,
        est.user_cambio_est, est.codpos, est.fec_nac_est, est.turno_est, est.generacion_est, est.periodo_est, est.anio_est, est.estado_civil_est, est.mat_tutor_est, est.pat_tutor_est,  est.nombre_tutor_est, est.no_folio_est, est.trabaja_est, est.tipo_sangre_est, est.id_tipo_esc_est, est.id_area_bach_est, est.fecha_ini_bach,
        est.fecha_fin_bach, est.promedio_gral_bach, est.tel_trabajo, est.edad_est, est.fecha_vig_est, est.estatus_inscri_est, est.imss_est,  est.clinica_est, est.num_servicio, est.fec_ser_social, est.fecha_repos_est, est.matri_est, est.beca_pro_est,  est.usuario_est, est.password_est, est.estatus_biblio, est.tipo_carrera_est, est.otras_uts, est.no_cedula_tsu, est.no_referencia, est.grasc,
        est.institucion_seguro, est.otrainstitucionseguro, est.nacionalidad, est.discapacidad, est.tipodiscapacidad, est.foliocertificado, est.fechaexpedicioncer, est.equivalencia, est.parentescotutor, est.tipoestudiante, est.num_ext, est.num_int, est.estatus_est ])
    return response
# Exportar paises a xlwt
@login_required
def export_xlwt_estudiante (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListarEstudiante.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicador')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Becas', 'Carrera', 'Colonia','Municipio','Escuela de Procedencia', 'Grupo','Id Estado', 'Matricula', 'Nombre(s)', 'Apellido paterno', 'Apelido materno', 'RFC', 'CURP','Direccion', 'Telefono', 'Correo electronico', 'Sexo','Fecha de alta', 'Usuario que dio alta', 'Fecha de baja', 'Uusuario que dio de baja', 'Codigo postal','Fecha de nacimiento','Turno','Generacion','Periodo', 'Año de ingreso', 'Estado civil',  'Apellido materno del tutor', 'Apellido paterno del tutor', 'Folio del estudiante', 'Trabajo del estudiante', 'Tipo de sangre', 'Tipo de escuela', 'Área del bachillerato', 'Fecha de inicio del bachillerato', 'Fecha de fin del bachillerato', 'Promedio general del bachillerato', 'Telefono del trabajo', 'Edad del estudiante',  'Fecha de vigencia', 'Estatus de inscrito al Imms', 'Imss', 'Clinica', 'Numero de servicio', 'Fecha del servicio social','Fecha ', 'Matricula provicional',  'Beca de aprovechamiento', 'Usuario', 'Contraseña', 'Estatus de biblioteca', 'Tipo de carrera', 'Otras', 'Cedula del TSU', 'Referencia', 'Grasc', 'Institucion del seguro', 'Otras Op','Nacionalidad', 'Discapacidad', 'Tipo de discapacidad',  'Folio certificado', 'Fecha',  'Equivalencia',  'Parentesco tutor','Tipo de estudiante', 'Num exterior', 'Numero interior', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeTabEstudiante.objects.filter(estatus_est="A").values_list('rowid_becas', 'rowid_car', 'rowid_col','rowid_mundel','rowid_esc_proc', 'rowid_grupo', 'id_matricula', 'nombre_estu',
    'paterno_est', 'materno_est', 'rfc_est', 'curp_est', 'direccion_est', 'telefono_est', 'email_est', 'sexo_est', 'fecha_alta_est', 'user_alta_est',
    'fecha_cambio_est', 'user_cambio_est', 'codpos', 'fec_nac_est', 'turno_est', 'generacion_est', 'periodo_est', 'anio_est',
    'estado_civil_est', 'mat_tutor_est', 'pat_tutor_est', 'nombre_tutor_est', 'no_folio_est', 'trabaja_est', 'tipo_sangre_est',
    'id_tipo_esc_est', 'id_area_bach_est', 'fecha_ini_bach', 'fecha_fin_bach', 'promedio_gral_bach', 'tel_trabajo',
    'edad_est', 'fecha_vig_est', 'estatus_inscri_est', 'imss_est', 'clinica_est', 'num_servicio', 'fec_ser_social', 'fecha_repos_est',
    'matri_est', 'beca_pro_est', 'usuario_est', 'password_est', 'estatus_biblio', 'tipo_carrera_est', 'otras_uts',
    'no_cedula_tsu', 'no_referencia', 'grasc', 'institucion_seguro', 'otrainstitucionseguro', 'nacionalidad',
    'discapacidad', 'tipodiscapacidad', 'foliocertificado', 'fechaexpedicioncer', 'equivalencia', 'parentescotutor', 'tipoestudiante',
    'num_ext', 'num_int', 'estatus_est')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################################### DOCUMENTACION ##############################################
# VISUALIZACION
@login_required
def vista_Documentacion(request):
    listaDoc=SeCatDocumentacion.objects.filter(estatus_doc="A").order_by('rowid_doc') 
    contador_id = listaDoc.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaDoc, 6)
        listaDoc = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormDocumentacion(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            ultimo_id = SeCatDocumentacion.objects.all().order_by('rowid_doc').last() 
            doc.rowid_doc = ultimo_id.rowid_doc + 1
            doc.save()
            messages.success(request, "¡Documentacion agregada con exito!")
            return redirect('vista_Documentacion')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Documentacion/GestionDoc.html",{'entity' : listaDoc, 'paginator' : paginator, 'FormDocumentacion' : form, 'contador': contador_id,})       
    #Busqueda del search
    elif request.method =='GET':
        busqueda = request.GET.get("search_doc", None)
        print(busqueda)
        if busqueda:
            listaDoc = SeCatDocumentacion.objects.filter(
                Q(descri_corto_doc__icontains = busqueda),
                Q(estatus_doc__icontains = "A")
            ).distinct()
    form = FormDocumentacion()
    data = {
        'entity' : listaDoc,
        'paginator' : paginator,
        'FormDocumentacion' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/Documentacion/GestionDoc.html",data)
# ELIMINA
@login_required
def eliminar_Documentacion(request, rowid_doc):
    try:
        doc = SeCatDocumentacion.objects.get(rowid_doc=rowid_doc)
        doc.estatus_doc = "B"
    except SeCatDocumentacion.DoesNotExist:
        raise Http404("El documento no existe")
    if request.method == 'POST':
        messages.warning(request, "¡Documento eliminado con exito!")
        doc.save()
        return redirect('vista_Documentacion')
    return render(request, "controlEscolar/catalogos/estudiantes/Documentacion/BorrarDoc.html", {"Doc": doc})
# MODIFICA 
@login_required
def vista_Documentacion_detail(request, rowid_doc):
    doc = SeCatDocumentacion.objects.get(rowid_doc = rowid_doc)
    form = FormDocumentacion(instance = doc)
    if request.method == 'POST':
        form = FormDocumentacion(request.POST, instance = doc) 
        if form.is_valid():
            doc = form.save(commit=False)
            doc.save()
            messages.info(request, "¡Documento actualizado con exito!")
            return redirect('vista_Documentacion')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Documentacion/ActualizarDoc.html", {"FormDocumentacion": form})
    return render(request, "controlEscolar/catalogos/estudiantes/Documentacion/ActualizarDoc.html", {"FormDocumentacion": form})
# PRINT
class Export_print_Documentacion(View):
    def get(self, request, *args, **kwargs):
        listaDoc=SeCatDocumentacion.objects.filter(estatus_doc="A") 
        data = {
            'count': listaDoc.count(),
            'documentos': listaDoc
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Documentacion/ListaDoc.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# PDF
class Export_pdf_Documentacion(View):
    def get(self, request,*args, **kwargs):
        listaDoc=SeCatDocumentacion.objects.filter(estatus_doc="A") 
        data = {
            'count': listaDoc.count(),
            'documentos': listaDoc
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Documentacion/ListaDoc.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaDocumentos.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# CSV 
@login_required
def export_csv_Documentacion (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaDocumentos.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave Doc','Nombre Doc','Abreviatura Doc','Importancia Doc','Clave CTRL Doc','CTG Doc','Estatus'])
    listaDoc=SeCatDocumentacion.objects.filter(estatus_doc="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for doc in listaDoc:
        writer.writerow([doc.id_doc, doc.descri_largo_doc, doc.descri_corto_doc , doc.importante_doc, doc.cve_control_doc, doc.estatus_grado, doc.estatus_doc])
    return response
# XLWT
@login_required
def export_xlwt_Documentacion (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaDocumentos.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Indicador')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave Doc','Nombre Doc','Abreviatura Doc','Importancia Doc','Clave CTRL Doc','CTG Doc','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatDocumentacion.objects.filter(estatus_doc="A").values_list('id_doc','descri_largo_doc', 'descri_corto_doc', 'importante_doc', 'cve_control_doc', 'estatus_grado', 'estatus_doc')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################################### GRUPO ######################################################
# VISUALIZACION
@login_required
def vista_Grupo(request):
    listaGrupos=SeCatGrupo.objects.filter(estatus_gpo="A").order_by('rowid_grupo') 
    contador_id = listaGrupos.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaGrupos, 6)
        listaGrupos = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormGrupo(request.POST)
        if form.is_valid():
            gru = form.save(commit=False)
            ultimo_id = SeCatGrupo.objects.all().last()
            gru.rowid_grupo = ultimo_id.rowid_grupo + 1
            form.save()
            messages.success(request, "¡Grupo agregado con exito!")
            return redirect('vista_Grupo')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Grupos/GestionGrupo.html",{ 'entity' : listaGrupos, 'paginator' : paginator, 'FormGrupo' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method =='GET':
        busqueda = request.GET.get("search_grupos", None)
        print(busqueda)
        if busqueda:
            listaGrupos = SeCatGrupo.objects.filter(
                Q(descri_largo_gpo__icontains = busqueda),
                Q(estatus_gpo__icontains = "A")
            ).distinct()
    form = FormGrupo()
    data = {
        'entity' : listaGrupos,
        'paginator' : paginator,
        'FormGrupo' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/Grupos/GestionGrupo.html",data)
# ELIMINA
@login_required
def eliminar_Grupo(request, rowid_grupo):
    try:
        grupo = SeCatGrupo.objects.get(rowid_grupo = rowid_grupo)
        grupo.estatus_gpo = "B"
    except SeCatGrupo.DoesNotExist:
        raise Http404("El grupo no existe")
    if request.method == 'POST':
        messages.warning(request, "¡Grupo eliminado con exito!")
        grupo.save()
        return redirect('vista_Grupo')
    return render(request, "controlEscolar/catalogos/estudiantes/Grupos/BorraGrupo.html", {"Grupo": grupo})
# MODIFICA
@login_required
def vista_grupo_detail(request, rowid_grupo):
    grupo = SeCatGrupo.objects.get(rowid_grupo = rowid_grupo)
    form = FormGrupo(instance = grupo)
    if request.method == 'POST':
        form = FormGrupo(request.POST, instance = grupo) 
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()
            messages.info(request, "¡Grupo actualizado con exito!")
            return redirect('vista_Grupo')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Grupos/ActualizarGrupo.html", {"FormGrupo": form})
    return render(request, "controlEscolar/catalogos/estudiantes/Grupos/ActualizarGrupo.html", {"FormGrupo": form})
# PRINT
class Export_print_grupos(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaGrupo=SeCatGrupo.objects.filter(estatus_gpo="A") 
        data = {
            'count': listaGrupo.count(),
            'Grupos': listaGrupo
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Grupos/ListaGrupo.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# PDF
class Export_pdf_grupo(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaGrupo=SeCatGrupo.objects.filter(estatus_gpo="A") 
        data = {
            'count': listaGrupo.count(),
            'Grupos': listaGrupo
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Grupos/ListaGrupo.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaGrupos.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# CSV 
@login_required
def export_csv_grupos (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaGrupos.csv;'
    writer = csv.writer(response)
    writer.writerow(['Carrera', 'Grado', 'Clave Grupo', 'Nombre', 'Abreviatura', 'Total de Alumnos','Máx. de Alumnos','Total de Recursadores','Máx. de Recursadores','Estatus'])
    listaGrupo=SeCatGrupo.objects.filter(estatus_gpo="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for gru in listaGrupo:
        writer.writerow([gru.rowid_car, gru.rowid_grado, gru.id_grupo, gru.descri_largo_gpo, gru.descri_corto_gpo, gru.lim_gpo, gru.lim_acu_gpo, gru.lim_rec_gpo, gru.lim_acu_rec_gpo, gru.estatus_gpo])
    return response
# XLWT
@login_required
def export_xlwt_grupos (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaGrupos.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Grupos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Carrera', 'Grado', 'Clave Grupo', 'Nombre', 'Abreviatura', 'Total de Alumnos','Máx. de Alumnos','Total de Recursadores','Máx. de Recursadores','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatGrupo.objects.filter(estatus_gpo="A").values_list('rowid_car','rowid_grado','id_grupo','descri_largo_gpo','descri_corto_gpo','lim_gpo','lim_acu_gpo','lim_rec_gpo','lim_acu_rec_gpo','estatus_gpo')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################################### ESTATUS ESTUDIANTE #########################################
# VISUALIZACION
@login_required
def vista_Estatus(request): 
    listaEst=SeCatEstatusEstudiante.objects.filter(estatus_tipo_est="A").order_by('rowid_evento_est') 
    contador_id = listaEst.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaEst, 6)
        listaEst = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormEstatusEstudiante(request.POST)
        if form.is_valid():
            est = form.save(commit=False)
            ultimo_id = SeCatEstatusEstudiante.objects.all().last() 
            est.rowid_evento_est = ultimo_id.rowid_evento_est + 1
            est.save()
            messages.success(request, "Estatus-Estudiante agregado con exito!")
            return redirect('vista_Estatus')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Estatus/GestionEstatus.html",{'entity' : listaEst, 'paginator' : paginator, 'FormEstatusEstudiante' : form, 'contador': contador_id,})       
    #Busqueda del search
    elif request.method =='GET':
        busqueda = request.GET.get("search_est", None)
        print(busqueda)
        if busqueda:
            listaEst = SeCatEstatusEstudiante.objects.filter(
                Q(descri_corto_tipo_est__icontains = busqueda),
                Q(estatus_tipo_est__icontains = "A")
            ).distinct()
    form = FormEstatusEstudiante()
    data = {
        'entity' : listaEst,
        'paginator' : paginator,
        'FormEstatusEstudiante' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/Estatus/GestionEstatus.html",data)
# ELIMINA
@login_required
def eliminar_Estatus(request, rowid_evento_est):
    try:
        est = SeCatEstatusEstudiante.objects.get(rowid_evento_est = rowid_evento_est)
        est.estatus_tipo_est = "B"
    except SeCatEstatusEstudiante.DoesNotExist:
        raise Http404("Estatus-Estudiante no existe")
    if request.method == 'POST':
        messages.warning(request, "¡Estatus-Estudiante eliminado con exito!")
        est.save()
        return redirect('vista_Estatus')
    return render(request, "controlEscolar/catalogos/estudiantes/Estatus/BorrarEstatus.html", {"Est": est})
# MODIFICA
@login_required
def vista_Estatus_detail(request, rowid_evento_est):
    est = SeCatEstatusEstudiante.objects.get(rowid_evento_est = rowid_evento_est)
    form = FormEstatusEstudiante(instance = est)
    if request.method == 'POST':
        form= FormEstatusEstudiante(request.POST, instance = est) 
        if form.is_valid():
            est = form.save(commit=False)
            est.save()
            messages.info(request, "¡Estatus-Estudiante actualizado con exito!")
            return redirect('vista_Estatus')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Estatus/ActualizarEstatus.html", {"FormEstatusEstudiante": form})
    return render(request, "controlEscolar/catalogos/estudiantes/Estatus/ActualizarEstatus.html", {"FormEstatusEstudiante": form})
# PRINT
class Export_print_estatus(View):
    def get(self, request, *args, **kwargs):
        listaEst=SeCatEstatusEstudiante.objects.filter(estatus_tipo_est="A") 
        data = {
            'count': listaEst.count(),
            'Estatus': listaEst
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Estatus/ListaEstatus.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# PDF
class Export_pdf_estatus(View):
    def get(self, request,*args, **kwargs):
        listaEst=SeCatEstatusEstudiante.objects.filter(estatus_tipo_est="A") 
        data = {
            'count': listaEst.count(),
            'Estatus': listaEst
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Estatus/ListaEstatus.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaEstatusEstudiantes.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# CSV
@login_required
def export_csv_estatus (request): 
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaEstatusEstudiantes.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave','Consecutivo','Nombre','Abreviatura','Estatus'])
    listaEst=SeCatEstatusEstudiante.objects.filter(estatus_tipo_est="A") 
    for esta in listaEst:
        writer.writerow([esta.id_evento_est, esta.consecutivo_est, esta.descri_largo_tipo_est, esta.descri_corto_tipo_est, esta.estatus_tipo_est ])
    return response
# XLWT
@login_required
def export_xlwt_estatus (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListarEstatusEstudiantes.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('EstatusEstudiantes')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave','Consecutivo','Nombre','Abreviatura','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatEstatusEstudiante.objects.filter(estatus_tipo_est="A").values_list('id_evento_est', 'consecutivo_est', 'descri_largo_tipo_est', 'descri_corto_tipo_est', 'estatus_tipo_est')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################################### GRADOS ##############################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_Grados(request):
    listaGrados=SeCatGrado.objects.filter(estatus_gra="A").order_by('rowid_grado')
    contador_id = listaGrados.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaGrados, 9)
        listaGrados = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormGrados(request.POST)
        if form.is_valid():
            grado = form.save(commit=False)
            ultimo_id = SeCatGrado.objects.all().order_by('rowid_grado').last() 
            grado.rowid_grado = ultimo_id.rowid_grado + 1 
            grado.save()
            messages.success(request, "¡Grado agregado con exito!")
            return redirect('vista_Grados') 
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Grados/GestionGrados.html",{'entity' : listaGrados, 'paginator' : paginator, 'FormGrados' : form, 'contador': contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_grados", None)
        print(busqueda)
        if busqueda:
            listaGrados = SeCatGrado.objects.filter(
                Q(descri_corto_gra__icontains = busqueda),
                Q(estatus_gra__icontains = "A")
            ).distinct()
    form = FormGrados()
    data = {
        'entity' : listaGrados,
        'paginator' : paginator,
        'FormGrados' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/Grados/GestionGrados.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminar_Grado(request, rowid_grado):
    try:
        grado = SeCatGrado.objects.get(rowid_grado=rowid_grado)
        grado.estatus_gra = "B"
    except SeCatGrado.DoesNotExist:
        raise Http404("El Grado no existe")
    if request.method == 'POST':
        grado.save()
        messages.warning(request, "¡Grado eliminado con exito!")
        return redirect('vista_Grados')
    return render(request, "controlEscolar/catalogos/estudiantes/Grados/BorrarGrado.html", {"Grado": grado})
# Modifica un registro
@login_required
def vista_grados_detail(request, rowid_grado):
    grado = SeCatGrado.objects.get(rowid_grado=rowid_grado)
    form = FormGrados(instance=grado)
    if request.method == 'POST':
        form = FormGrados(request.POST, instance = grado)
        if form.is_valid():
            grado = form.save(commit=False)
            grado.save()
            messages.info(request, "¡Grado actualizado con exito!")
            return redirect('vista_Grados')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/estudiantes/Grados/ActualizarGrado.html", {"FormGrados" : form})
    return render(request, "controlEscolar/catalogos/estudiantes/Grados/ActualizarGrado.html", {"FormGrados" : form})
# primera de pdf posible imprimir 
class Export_print_grados(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaGrados=SeCatGrado.objects.filter(estatus_gra="A") 
        data = {
            'count': listaGrados.count(),
            'grados': listaGrados
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Grados/ListarGrados.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las grados
class Export_pdf_grado(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaGrados=SeCatGrado.objects.filter(estatus_gra="A") 
        data = {
            'count': listaGrados.count(),
            'grados': listaGrados
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Grados/ListarGrados.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaGrados.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria
@login_required
def export_csv_grados (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaGrados.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave grado', 'Descripción', 'Estatus'])
    listaGrados=SeCatGrado.objects.filter(estatus_gra="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for gra in listaGrados:
        writer.writerow([gra.id_grado, gra.descri_corto_gra, gra.estatus_gra])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_grados (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaGrados.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Grados')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave grado', 'Descripción', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatGrado.objects.filter(estatus_gra="A").values_list('id_grado', 'descri_corto_gra', 'estatus_gra')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

####################################################  SALONES  ######################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_Salones(request):
    listaSalones = SeCatSalones.objects.filter(estatus_salon="A").order_by('rowid_salon')
    contador_id = listaSalones.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaSalones, 9)
        listaSalones = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormSalones(request.POST)
        if form.is_valid():
            sal = form.save(commit=False)
            ultimo_id = SeCatSalones.objects.all().order_by('rowid_salon').last()
            sal.rowid_salon = ultimo_id.rowid_salon + 1
            sal.save()
            messages.success(request, "¡Salón agregado con exito!")
            return redirect('vista_Salones')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Salones/GestionSalones.html",{'entity' : listaSalones, 'paginator' : paginator, 'FormSalones' : form, 'contador': contador_id,})       
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_salones", None)
        print(busqueda)
        if busqueda:
            listaSalones = SeCatSalones.objects.filter(
                Q(descri_largo_salon__icontains = busqueda),
                Q(estatus_salon__icontains = "A")
            ).distinct()
    form = FormSalones()
    data = {
        'entity' : listaSalones,
        'paginator' : paginator,
        'FormSalones' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/Salones/GestionSalones.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminar_Salones(request, rowid_salon):
    try:
        sal = SeCatSalones.objects.get(rowid_salon=rowid_salon)
        sal.estatus_salon = "B"
    except SeCatSalones.DoesNotExist:
        raise Http404("El Salón no existe")
    if request.method == 'POST':
        sal.save()
        messages.warning(request, "¡Salón eliminado con exito!")
        return redirect('vista_Salones')
    return render(request, "controlEscolar/catalogos/estudiantes/Salones/BorrarSalones.html", {"Salon": sal})
# Modifica un registro
@login_required
def vista_salones_detail(request, rowid_salon):
    sa = SeCatSalones.objects.get(rowid_salon=rowid_salon)
    form = FormSalones(instance = sa)
    if request.method == 'POST':
        form = FormSalones(request.POST, instance = sa)
        if form.is_valid():
            sa = form.save(commit=False)
            sa.save()
            messages.info(request, "¡Salón actualizada con exito!")
            return redirect('vista_Salones')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/estudiantes/Salones/ActualizarSalones.html", {"FormSalones" : form})
    return render(request, "controlEscolar/catalogos/estudiantes/Salones/ActualizarSalones.html", {"FormSalones" : form})
# primera de pdf posible imprimir 
class Export_print_salones(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaSalones = SeCatSalones.objects.filter(estatus_salon="A")
        data = {
            'count': listaSalones.count(),
            'salones': listaSalones
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Salones/listaSalones.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las salones
class Export_pdf_salones(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaSalones=SeCatSalones.objects.filter(estatus_salon="A")
        data = {
            'count': listaSalones.count(),
            'salones': listaSalones
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Salones/listaSalones.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaSalones.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria
@login_required
def export_csv_salones (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaSalones.csv;'
    writer = csv.writer(response)
    writer.writerow(['Carrera','Clave Salón','Nombre Salón','Abreviación Salón','Tipo Salón','Compartido','Estatus'])
    listaSalones=SeCatSalones.objects.filter(estatus_salon="A")
    for sal in listaSalones:
        writer.writerow([sal.rowid_car, sal.id_salon, sal.descri_largo_salon, sal.descri_corto_salon, sal.tipo_salon,
                        sal.compartido_salon, sal.estatus_salon])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_salones (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaSalones.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Salones')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Carrera','Clave Salón','Nombre Salón','Abreviación Salón','Tipo Salón','Compartido','Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatSalones.objects.filter(estatus_salon="A").values_list('rowid_car','id_salon','descri_largo_salon','descri_corto_salon',
                                                                    'tipo_salon','compartido_salon','estatus_salon')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

# ###################################################   Becas  ######################################################
# Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_Becas(request):
    listaBecas=SeCatBecas.objects.filter(estatus_bec="A").order_by('rowid_becas')
    contador_id = listaBecas.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaBecas, 9)
        listaBecas = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormBecas(request.POST)
        if form.is_valid():
            beca = form.save(commit=False)
            ultimo_id = SeCatBecas.objects.all().order_by('rowid_becas').last()
            beca.rowid_becas = ultimo_id.rowid_becas + 1
            beca.save()
            messages.success(request, "¡Beca agregada con exito!")
            return redirect('vista_Becas')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/Becas/GestionBecas.html",{'entity' : listaBecas,'paginator' : paginator,'FormBecas' : form,'contador' : contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_becas", None)
        print(busqueda)
        if busqueda:
            listaBecas = SeCatBecas.objects.filter(
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
@login_required
def eliminar_Beca(request, rowid_becas):
    try:
        beca = SeCatBecas.objects.get(rowid_becas=rowid_becas)
        beca.estatus_bec = "B"
    except SeCatBecas.DoesNotExist:
        raise Http404("La Beca no existe")
    if request.method == 'POST':
        beca.save()
        messages.warning(request, "¡Beca eliminada con exito!")
        return redirect('vista_Becas')
    return render(request, "controlEscolar/catalogos/estudiantes/Becas/BorrarBeca.html", {"Beca": beca})
# Modifica un registro
@login_required
def vista_becas_detail(request, rowid_becas):
    beca = SeCatBecas.objects.get(rowid_becas=rowid_becas)
    form = FormBecas(instance=beca)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormBecas(request.POST, instance = beca)
        if form.is_valid():
            beca = form.save(commit=False)
            beca.save()
            messages.info(request, "¡Beca actualizada con exito!")
            return redirect('vista_Becas')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/estudiantes/Becas/ActualizarBeca.html", {"FormBecas" : form})
    return render(request, "controlEscolar/catalogos/estudiantes/Becas/ActualizarBeca.html", {"FormBecas" : form})
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_becas(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaBecas=SeCatBecas.objects.filter(estatus_bec="A") 
        data = {
            'count': listaBecas.count(),
            'becas': listaBecas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/Becas/listaBecas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_becas(LoginRequiredMixin, View):
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
@login_required
def export_csv_becas (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaBecas.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave Beca', 'Valor Inicial', 'Valor Final', 'Porcentaje', 'Estatus'])
    listaBecas=SeCatBecas.objects.filter(estatus_bec="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for bs in listaBecas:
        writer.writerow([bs.id_becas, bs.valor_ini_bec, bs.valor_fin_bec, bs.porcentaje_beca, bs.estatus_bec])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_becas (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaBecas.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Becas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave Beca', 'Valor Inicial', 'Valor Final', 'Porcentaje', 'Estatus']
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

###################################################   Tipo Cambio  ################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_Cambios(request):
    listaCambios = SeCatTipoCambio.objects.filter(status="A").order_by('rowid_tipo_cambio')
    contador_id = listaCambios.count() 
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaCambios, 9)
        listaCambios = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormTipoCambio(request.POST)
        if form.is_valid():
            cambio = form.save(commit=False)
            ultimo_id = SeCatTipoCambio.objects.all().order_by('rowid_tipo_cambio').last() 
            cambio.rowid_tipo_cambio = ultimo_id.rowid_tipo_cambio + 1 
            form.save()
            messages.success(request, "¡Tipo de Cambio agregaoa con exito!")
            return redirect('vista_Cambios')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/GestionTipoCambios.html",{'entity' : listaCambios,'paginator' : paginator,'FormTipoCambio' : form,'contador': contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_cambios", None)
        print(busqueda)
        if busqueda:
            listaCambios = SeCatTipoCambio.objects.filter(
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
@login_required
def eliminar_Cambio(request, rowid_tipo_cambio):
    try:
        cambio = SeCatTipoCambio.objects.get(rowid_tipo_cambio=rowid_tipo_cambio)
        cambio.status = "B"
    except SeCatTipoCambio.DoesNotExist:
        raise Http404("El Tipo de Cambio no existe")
    if request.method == 'POST':
        cambio.save()
        messages.warning(request, "¡Tipo de Cambio eliminado con exito!")
        return redirect('vista_Cambios')
    return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/BorrarTipoCambio.html", {"Cambio": cambio})
# Modifica un registro
@login_required
def vista_cambios_detail(request, rowid_tipo_cambio):
    cambio = SeCatTipoCambio.objects.get(rowid_tipo_cambio=rowid_tipo_cambio)
    form = FormTipoCambio(instance=cambio)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormTipoCambio(request.POST, instance = cambio)
        if form.is_valid():
            cambio.save()
            messages.info(request, "¡Tipo de Cambio actualizado con exito!")
            return redirect('vista_Cambios')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/ActualizarTipoCambio.html", {"FormTipoCambio" : form}) #envia al detalle de errores
    return render(request, "controlEscolar/catalogos/estudiantes/TipoCambio/ActualizarTipoCambio.html", {"FormTipoCambio" : form}) #envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_cambios(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaCambios=SeCatTipoCambio.objects.filter(status="A") 
        data = {
            'count': listaCambios.count(),
            'cambios': listaCambios
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/TipoCambio/listaTiposCambios.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_cambios(LoginRequiredMixin, View):
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
@login_required
def export_csv_cambios (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposCambios.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave Tipo Cambio', 'Descripción Tipo Cambio', 'Estatus'])
    listaCambios=SeCatTipoCambio.objects.filter(status="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for lc in listaCambios:
        writer.writerow([lc.id_tipo_cambio, lc.descri_tipocambio, lc.status])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_cambios (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposCambios.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tipos de Cambio')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave Tipo Cambio', 'Descripción Tipo Cambio', 'Estatus']
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

##############################################  Tipos de Baja #####################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vista_TipoBajas(request):
    listaBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A").order_by('rowid_tipo_baj')
    contador_id = listaBajas.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaBajas, 9)
        listaBajas = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormTipoBajas(request.POST)
        if form.is_valid():
            baja = form.save(commit=False)
            ultimo_id = SeCatTipoBajas.objects.all().order_by('rowid_tipo_baj').last() 
            baja.rowid_tipo_baj = ultimo_id.rowid_tipo_baj + 1 
            baja.save()
            messages.success(request, "¡Tipo de Baja agregada con exito!")
            return redirect('vista_TipoBajas') 
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/estudiantes/TipoBajas/GestionTipoBajas.html",{'entity' : listaBajas, 'paginator' : paginator, 'FormTipoBajas' : form, 'contador': contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_bajas", None)
        print(busqueda)
        if busqueda:
            listaBajas = SeCatTipoBajas.objects.filter(
                Q(descri_largo_tipo_baj__icontains = busqueda),
                Q(estatus_tipo_baj__icontains = "A")
            ).distinct()
    form = FormTipoBajas()
    data = {
        'entity' : listaBajas,
        'paginator' : paginator,
        'FormTipoBajas' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/estudiantes/TipoBajas/GestionTipoBajas.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminar_TipoBajas(request, rowid_tipo_baj):
    try:
        baja = SeCatTipoBajas.objects.get(rowid_tipo_baj=rowid_tipo_baj)
        baja.estatus_tipo_baj = "B"
    except SeCatTipoBajas.DoesNotExist:
        raise Http404("El Tipo de Baja no existe")
    if request.method == 'POST':
        baja.save()
        messages.warning(request, "¡Tipo de Baja eliminada con exito!")
        return redirect('vista_TipoBajas')
    return render(request, "controlEscolar/catalogos/estudiantes/TipoBajas/BorrarTipoBajas.html", {"Baja": baja})
# Modifica un registro
@login_required
def vista_tipobajas_detail(request, rowid_tipo_baj):
    baja = SeCatTipoBajas.objects.get(rowid_tipo_baj=rowid_tipo_baj)
    form = FormTipoBajas(instance=baja)
    if request.method == 'POST':
        form = FormTipoBajas(request.POST, instance = baja)
        if form.is_valid():
            baja = form.save(commit=False)
            baja.save()
            messages.info(request, "¡Tipo de Baja actualizada con exito!")
            return redirect('vista_TipoBajas')
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/estudiantes/TipoBajas/ActualizarTipoBajas.html", {"FormTipoBajas" : form})
    return render(request, "controlEscolar/catalogos/estudiantes/TipoBajas/ActualizarTipoBajas.html", {"FormTipoBajas" : form})
# primera de pdf posible imprimir 
class Export_print_tipobajas(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A") 
        data = {
            'count': listaBajas.count(),
            'bajas': listaBajas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/TipoBajas/listaTipoBajas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las grados
class Export_pdf_tipobajas(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A") 
        data = {
            'count': listaBajas.count(),
            'bajas': listaBajas
        }
        pdf = render_to_pdf('controlEscolar/catalogos/estudiantes/TipoBajas/listaTipoBajas.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaTiposdeBaja.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria
@login_required
def export_csv_tipobajas (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposdeBaja.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave Tipo Baja', 'Descripción', 'Abreviatura', 'Estatus'])
    listaBajas=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A") 
    # listaPaises=SeCatPais.objects.filter(owner=request.user)
    for ba in listaBajas:
        writer.writerow([ba.id_tipo_baj, ba.descri_largo_tipo_baj, ba.descri_corto_tipo_baj, ba.estatus_tipo_baj])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT
@login_required
def export_xlwt_tipobajas (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaTiposdeBaja.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Bajas')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave Tipo Baja', 'Descripción', 'Abreviatura', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatTipoBajas.objects.filter(estatus_tipo_baj="A").values_list('id_tipo_baj', 'descri_largo_tipo_baj', 'descri_corto_tipo_baj', 'estatus_tipo_baj')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

# -------------------------------------------- Empleados --------------------------------------------- #

###################################### Empleados #################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaEmpleados(request):
    listaEmp = SeCatEmpleado.objects.filter(estatus_emp="A"). order_by('rowid_empleado')#Lista de todas las divisiones
    contador_id = listaEmp.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaEmp, 9)
        listaEmp = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormEmpleado(request.POST)
        if form.is_valid():
            emp = form.save(commit=False)
            ultimo_id = SeCatEmpleado.objects.all().order_by('rowid_empleado').last()
            emp.rowid_empleado = ultimo_id.rowid_empleado + 1
            emp.save()
            messages.success(request, "¡Empleado agregado con exito!")
            return redirect('vista_emp')#redirecciona a la vista 
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/empleados/GestionEmpleados/GestionEmpleados.html",{'entity' : listaEmp, 'paginator' : paginator, 'FormEmpleado' : form, 'contador': contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_emp", None)
        if busqueda:
            listaEmp = SeCatEmpleado.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(nombre_emp__icontains = busqueda),
                Q(estatus_emp__icontains = "A")
            ).distinct()
    form = FormEmpleado()
    data = {
        'entity' : listaEmp,
        'paginator' : paginator,
        'FormEmpleado' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionEmpleados/GestionEmpleados.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarEmpleado(request, rowid_empleado):
    try:
        emp = SeCatEmpleado.objects.get(rowid_empleado=rowid_empleado)
        emp.estatus_emp = "B"
    except SeCatEmpleado.DoesNotExist:
        raise Http404("El empleado no existe")
    if request.POST: #Sobre escribe los valores
        messages.warning(request, "¡Empleado eliminado con exito!")
        emp.save()
        return redirect('vista_emp')
    return render(request, "controlEscolar/catalogos/empleados/GestionEmpleados/BorrarEmpleados.html", {"emp": emp})
# Modifica un registro
@login_required
def vista_emp_detail(request, rowid_empleado):
    emp = SeCatEmpleado.objects.get(rowid_empleado=rowid_empleado)
    form = FormEmpleado(instance = emp)
    if request.method == 'POST': #Sobre escribe los valores
        form = FormEmpleado(request.POST, instance = emp)
        if form.is_valid():
            messages.info(request, "¡Empleado actualizado con exito!")
            form.save()
            return redirect('vista_emp') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/empleados/GestionEmpleados/ActualizarEmpleados.html", {"FormEmpleado" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/empleados/GestionEmpleados/ActualizarEmpleados.html", {"FormEmpleado" : form})#envia al detalle para actualizar
# Imprimir 
class Export_print_emp(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        listaEmp = SeCatEmpleado.objects.filter(estatus_emp="A") 
        data = {
            'count': listaEmp.count(),
            'emp': listaEmp
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionEmpleados/listaEmpleados.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_emp(LoginRequiredMixin,View):
    def get(self, request,*args, **kwargs):
        listaEmp=SeCatEmpleado.objects.filter(estatus_emp="A") 
        data = {
            'count': listaEmp.count(),
            'emp': listaEmp
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionEmpleados/listaEmpleados.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaEmpleados.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria 
@login_required
def export_csv_emp (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaEmpleados.csv;'
    writer = csv.writer(response)
    writer.writerow(['Nivel Academico','Carrera','Departamento','Estado de Nacimiento','Colonia','Sueldo','ID Empleado','Nombre','Apellido Paterno',
            'Apellido Materno','RFC','CURP','Direccion','Tel','Email','Sexo','Fecha Alta','User Alta','User Cambio','Fecha Cambio','Estatus Empleado'
            ,'C.P','Horas Contra','Fecha Nacimiento','Estatus Val','Estatus Comp','Edad Empleado','Estado Civil','Num Vac Max','Num Vac Act'
            ,'Tipo Contrato','Cedula','FecIcon','FecFcon','Comentario','Estatus Biblio'])
    listaEmp=SeCatEmpleado.objects.filter(estatus_emp="A") 
    for e in listaEmp:
        writer.writerow([e.rowid_academico,e.rowid_car,e.rowid_depto,e.rowid_edo,e.rowid_col,e.rowid_sueldo,e.id_empleado,e.nombre_emp,e.paterno_emp,e.materno_emp 
            ,e.rfc_emp,e.curp_emp,e.direccion_emp,e.telefono_emp,e.email_emp,e.sexo_emp,e.fecha_alta_emp,e.user_alta_emp,e.user_cambio_emp 
            ,e.fecha_cambio_emp,e.estatus_emp,e.codpos_emp,e.horas_contra_emp,e.fec_nac_emp,e.estatus_val,e.estatus_comp,e.edad_emp 
            ,e.estado_civil_emp,e.num_vac_max,e.num_vac_act,e.tipo_contrato_com,e.cedula_emp_com,e.fecicon,e.fecfcon,e.comentario_emp 
            ,e.estatus_biblio])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_emp (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaEmpleados.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Empleados')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Nivel Academico','Carrera','Departamento','Estado de Nacimiento','Colonia','Sueldo','ID Empleado','Nombre','Apellido Paterno',
            'Apellido Materno','RFC','CURP','Direccion','Tel','Email','Sexo','Fecha Alta','User Alta','User Cambio','Fecha Cambio','Estatus Empleado'
            ,'C.P','Horas Contra','Fecha Nacimiento','Estatus Val','Estatus Comp','Edad Empleado','Estado Civil','Num Vac Max','Num Vac Act'
            ,'Tipo Contrato','Cedula','FecIcon','FecFcon','Comentario','Estado de Nacimiento','Estatus Biblio']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatEmpleado.objects.filter(estatus_emp="A").values_list('rowid_academico','rowid_car','rowid_depto','rowid_edo','rowid_col','rowid_sueldo','id_empleado',
                                                                    'nombre_emp','paterno_emp','materno_emp','rfc_emp','curp_emp','direccion_emp',
                                                                    'telefono_emp','email_emp','sexo_emp','fecha_alta_emp','user_alta_emp','user_cambio_emp',
                                                                    'fecha_cambio_emp','estatus_emp','codpos_emp','horas_contra_emp','fec_nac_emp','estatus_val',
                                                                    'estatus_comp','edad_emp','estado_civil_emp','num_vac_max','num_vac_act','tipo_contrato_com',
                                                                    'cedula_emp_com','fecicon','fecfcon','comentario_emp','estatus_biblio')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################  Nivel Academico  ##################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaNivelAca(request):
    #Lista de todas las divisiones
    listaNivelAca = SeCatNivelAcademico.objects.filter(estatus_acade="A").order_by('rowid_academico')
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
            ultimo_id = SeCatNivelAcademico.objects.all().order_by('rowid_academico').last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            aca.rowid_academico =  ultimo_id.rowid_academico + 1 # agrega uno al ultimo id insertado
            form.save() # Guadar lo ingresadoa l formulario
            messages.success(request, "¡Nivel Academico agregada con exito!")
            return redirect('vista_nivelaca') #redirecciona a la vista 
        else :
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/GestionNivelAcademico.html",{'entity' : listaNivelAca,'paginator' : paginator,'FormNivAca' : form,'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_nivelaca", None)
        print(busqueda)
        if busqueda:
            listaNivelAca = SeCatNivelAcademico.objects.filter(
                #Revisión de los campos de la tabla en la BD
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
@login_required
def eliminarNivelAca(request, rowid_academico):
    try:
        aca = SeCatNivelAcademico.objects.get(rowid_academico=rowid_academico)
        aca.estatus_acade = "B"
    except SeCatNivelAcademico.DoesNotExist:
        raise Http404("El nivel academico no existe")
    if request.POST: #Sobre escribe los valores
        aca.save()
        messages.warning(request, "¡Nivel academico eliminado con exito!")
        return redirect('vista_nivelaca')
    return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/BorrarNivelAcademico.html", {"Academico": aca})
# Modifica un registro
@login_required
def vista_nivel_aca_detail(request, rowid_academico):
    aca = SeCatNivelAcademico.objects.get(rowid_academico=rowid_academico)
    form = FormNivAca(instance = aca)
    if request.POST: #Sobre escribe los valores
        form = FormNivAca(request.POST, instance = aca)
        if form.is_valid():
            form.save()
            messages.info(request, "¡Nivel academico actualizado con exito!")
            return redirect('vista_nivelaca') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/ActualizarNivelAcademico.html", {"FormNivAca" : form})#envia al detalle de errores
    return render(request, "controlEscolar/catalogos/empleados/GestionNivelAcademico/ActualizarNivelAcademico.html", {"FormNivAca" : form})#envia al detalle para actualizar
#Imprimir pfd
class Export_print_nivel_academico(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaNivelAca = SeCatNivelAcademico.objects.filter(estatus_acade="A") 
        data = {
            'count': listaNivelAca.count(),
            'aca': listaNivelAca
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionNivelAcademico/ListaNivelAcademico.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_nivel_academico(LoginRequiredMixin, View):
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
@login_required
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
@login_required
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
#Agregar si es post y lista de todos / Aqui va la paginación
@login_required
def vistaPlaza(request):
    #Lista de todas las divisiones
    listaPlaza = SeCatPlaza.objects.filter(estatus_plaza="A").order_by('rowid_plaza')
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
            ultimo_id = SeCatPlaza.objects.all().order_by('rowid_plaza').last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            plaza.rowid_plaza = ultimo_id.rowid_plaza + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "¡Plaza agregada con exito!") 
            return redirect('vista_plaza') #redirecciona a la vista
        else :
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/GestionPlazas.html",{'entity' : listaPlaza, 'paginator' : paginator, 'FormPlaza' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_plaza", None)
        if busqueda:
            listaPlaza = SeCatPlaza.objects.filter(
                #Revisión de los campos de la tabla en la BD
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
@login_required
def eliminarPlaza(request, rowid_plaza):
    try:
        pla = SeCatPlaza.objects.get(rowid_plaza=rowid_plaza)
        pla.estatus_plaza = "B"
    except SeCatPlaza.DoesNotExist:
        raise Http404("La plaza no existe")
    if request.POST: #Sobre escribe los valores
        pla.save()
        messages.warning(request, "¡Plaza eliminada con exito!")
        return redirect('vista_plaza')
    return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/BorrarPlazas.html", {"Plazas": pla})
# Modifica un registro
@login_required
def vista_plaza_detail(request, rowid_plaza):
    pla = SeCatPlaza.objects.get(rowid_plaza=rowid_plaza)
    form = FormPlaza(instance = pla)
    if request.POST: #Sobre escribe los valores
        form = FormPlaza(request.POST, instance = pla)
        if form.is_valid():
            form.save()
            messages.info(request, "¡Plaza actualizada con exito!")
            return redirect('vista_plaza') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/ActualizarPlazas.html", {"FormPlaza" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/empleados/GestionPlazas/ActualizarPlazas.html", {"FormPlaza" : form})#envia al detalle para actualizar
# imprime 
class Export_print_plaza(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaPlaza = SeCatPlaza.objects.filter(estatus_plaza="A") 
        data = {
            'count': listaPlaza.count(),
            'pla': listaPlaza
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionPlazas/listaPlazas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_plaza(LoginRequiredMixin, View):
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
@login_required
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
@login_required
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

#################### TIPO PUESTOS ######################
#Agregar si es post y lista de todos / Aqui va la paginación
@login_required
def vistaTipoPue(request):
    #Lista de todas las divisiones
    listaPue = SeCatTipoPuesto.objects.filter(estatus_pue="A").order_by('rowid_puesto')
    contador_id = listaPue.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaPue, 9)
        listaPue = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormsTipoPue(request.POST)
        if form.is_valid():
            pue = form.save(commit=False)
            ultimo_id = SeCatTipoPuesto.objects.all().order_by('rowid_puesto').last() # hace una consulta al ultimo registro insertado para poder crear el nuevo id 
            pue.rowid_puesto = ultimo_id.rowid_puesto + 1 # agrega uno al ultimo id insertado
            form.save()
            messages.success(request, "¡Puesto agregada con exito!") 
            return redirect('vista_tipopue') #redirecciona a la vista
        else :
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/empleados/GestionTipoPuesto/GestionTipoPuesto.html",{'entity' : listaPue, 'paginator' : paginator, 'FormsTipoPue' : form, 'contador' : contador_id,})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_pue", None)
        if busqueda:
            listaPue = SeCatTipoPuesto.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(descri_largo_pue__icontains = busqueda),
                Q(estatus_pue__icontains = "A")
            ).distinct()
    form = FormsTipoPue()
    data = {
        'entity' : listaPue,
        'paginator' : paginator,
        'FormsTipoPue' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionTipoPuesto/GestionTipoPuesto.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarTipoPue(request, rowid_puesto):
    try:
        pue = SeCatTipoPuesto.objects.get(rowid_puesto=rowid_puesto)
        pue.estatus_pue = "B"
    except SeCatTipoPuesto.DoesNotExist:
        raise Http404("El puesto no existe")
    if request.POST: #Sobre escribe los valores
        pue.save()
        messages.warning(request, "¡Puesto eliminado con exito!")
        return redirect('vista_tipopue')
    return render(request, "controlEscolar/catalogos/empleados/GestionTipoPuesto/BorrarPuesto.html", {"pue": pue})
# Modifica un registro
@login_required
def vista_tipopue_detail(request, rowid_puesto):
    pue = SeCatTipoPuesto.objects.get(rowid_puesto=rowid_puesto)
    form = FormsTipoPue(instance = pue)
    if request.POST: #Sobre escribe los valores
        form = FormsTipoPue(request.POST, instance = pue)
        if form.is_valid():
            form.save()
            messages.info(request, "¡Puesto actualizado con exito!")
            return redirect('vista_tipopue') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido") 
            return render(request, "controlEscolar/catalogos/empleados/GestionTipoPuesto/ActualizarPuesto.html", {"FormsTipoPue" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/empleados/GestionTipoPuesto/ActualizarPuesto.html", {"FormsTipoPue" : form})#envia al detalle para actualizar
# imprime 
class Export_print_tipopue(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaPue = SeCatTipoPuesto.objects.filter(estatus_pue="A") 
        data = {
            'count': listaPue.count(),
            'pue': listaPue
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionTipoPuesto/listaPuestos.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_tipopue(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaPue=SeCatTipoPuesto.objects.filter(estatus_pue="A") 
        data = {
            'count': listaPue.count(),
            'pue': listaPue
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionTipoPuesto/listaPuestos.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaPuestos.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria 
@login_required
def export_csv_tipopue (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaPuestos.csv;'
    writer = csv.writer(response)
    writer.writerow(['Plaza','ID', 'Puesto', 'Abreviatura', 'Estatus'])
    listaPue=SeCatTipoPuesto.objects.filter(estatus_pue="A") 
    for pue in listaPue:
        writer.writerow([pue.rowid_plaza,pue.id_puesto, pue.descri_largo_pue, pue.descri_corto_pue, pue.estatus_pue])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_tipopue (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaPuestos.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tipo de Puestos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Plazas','ID', 'Puesto', 'Abreviatura', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatTipoPuesto.objects.filter(estatus_pue="A").values_list('rowid_plaza','id_puesto', 'descri_largo_pue',
                                                                    'descri_corto_pue', 'estatus_pue')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

###################################### Sueldos #################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaSueldos(request):
    #Lista de todas las divisiones
    listaSu = SeCatSueldos.objects.filter(estatus_sueldo="A").order_by('rowid_sueldo')
    contador_id = listaSu.count()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(listaSu, 9)
        listaSu = paginator.page(page)
    except:
        raise Http404
    if request.method == 'POST':
        form = FormSueldo(request.POST)
        if form.is_valid():
            su = form.save(commit=False)
            ultimo_id = SeCatSueldos.objects.all().order_by('rowid_sueldo').last()
            su.rowid_sueldo = ultimo_id.rowid_sueldo + 1
            su.save()
            messages.success(request, "¡Sueldo agregado con exito!")
            #redirecciona a la vista 
            return redirect('vista_su')
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!")
            return render(request, "controlEscolar/catalogos/empleados/GestionSueldos/GestionSueldos.html",{'entity' : listaSu, 'paginator' : paginator, 'FormSueldo' : form, 'contador': contador_id})
    #Busqueda del search
    elif request.method == 'GET':
        busqueda = request.GET.get("search_su", None)
        if busqueda:
            listaSu = SeCatSueldos.objects.filter(
                #Revisión de los campos de la tabla en la BD
                Q(sueldo__icontains = busqueda),
                Q(estatus_sueldo__icontains = "A")
            ).distinct()
    form = FormSueldo()
    data = {
        'entity' : listaSu,
        'paginator' : paginator,
        'FormSueldo' : form,
        'contador' : contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionSueldos/GestionSueldos.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarSueldos(request, rowid_sueldo):
    try:
        su = SeCatSueldos.objects.get(rowid_sueldo=rowid_sueldo)
        su.estatus_sueldo = "B"
    except SeCatSueldos.DoesNotExist:
        raise Http404("El sueldo no existe")
    if request.method == 'POST': #Sobre escribe los valores
        messages.warning(request, "¡Sueldo eliminado con exito!")
        su.save()
        return redirect('vista_su')
    return render(request, "controlEscolar/catalogos/empleados/GestionSueldos/BorrarSueldos.html", {"su": su})
# Modifica un registro
@login_required
def vista_su_detail(request, rowid_sueldo):
    su = SeCatSueldos.objects.get(rowid_sueldo=rowid_sueldo)
    form = FormSueldo(instance = su)
    if request.method == 'POST': #Sobre escribe los valores
        form = FormSueldo(request.POST, instance = su)
        if form.is_valid():
            messages.info(request, "¡Sueldo actualizado con exito!")
            form.save()
            return redirect('vista_su') #retorna despues de actualizar
        else:
            messages.warning(request, "Algun campo no es valido")
            return render(request, "controlEscolar/catalogos/empleados/GestionSueldos/ActualizarSueldos.html", {"FormSueldo" : form})#envia al detalle para actualizar
    return render(request, "controlEscolar/catalogos/empleados/GestionSueldos/ActualizarSueldos.html", {"FormSueldo" : form})#envia al detalle para actualizar
# Imprimir
class Export_print_su(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        listaSu = SeCatSueldos.objects.filter(estatus_sueldo="A") 
        data = {
            'count': listaSu.count(),
            'su': listaSu
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionSueldos/listaSueldos.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Exporta a pdf las Carreras
class Export_pdf_su(LoginRequiredMixin,View):
    def get(self, request,*args, **kwargs):
        listaSu=SeCatSueldos.objects.filter(estatus_sueldo="A") 
        data = {
            'count': listaSu.count(),
            'su': listaSu
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionSueldos/listaSueldos.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaSueldos.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar divisiones a CSV sin libreria 
@login_required
def export_csv_su (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaSueldos.csv;'
    writer = csv.writer(response)
    writer.writerow(['Puesto', 'ID Sueldo', 'Sueldo', 'Estatus'])
    listaSu=SeCatSueldos.objects.filter(estatus_sueldo="A") 
    for s in listaSu:
        writer.writerow([s.rowid_puesto, s.id_sueldo, s.sueldo, s.estatus_sueldo])
    return response
# Exportar divisiones a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_su (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaSueldos.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sueldos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Puesto', 'ID Sueldo', 'Sueldo', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatSueldos.objects.filter(estatus_sueldo="A").values_list('rowid_sueldo','rowid_puesto','id_sueldo', 'sueldo', 'estatus_sueldo')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response


##############################################   Adscripcion   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaAdscripciones(request):
    listaAdscripcion = SeCatDeptoEmp.objects.filter(estatus_depto="A").order_by('rowid_depto')
    contador_id = listaAdscripcion.count() 
    page = request.GET.get('page', 1)  
    try:  
        paginator = Paginator(listaAdscripcion, 7)
        listaAdscripcion = paginator.page(page)
    except: 
        raise Http404
    if request.method == 'POST': 
        form = FormAdscripcion(request.POST) 
        if form.is_valid(): 
            ads = form.save(commit=False)
            ultimo_id = SeCatDeptoEmp.objects.all().order_by('rowid_depto').last() 
            ads.rowid_depto = ultimo_id.rowid_depto + 1 
            ads.save() 
            messages.success(request, "¡Adscripcion agregado con exito!")       
            return redirect('vista_adscripciones') 
        else: 
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionAdscripciones/GestionAdscripciones.html",{'entity' : listaAdscripcion,'paginator' : paginator,'FormAdscripcion' : form,'contador': contador_id})       
    elif request.method == 'GET': 
        busqueda = request.GET.get("search_adscripcion", None) 
        if busqueda: 
            listaAdscripcion = SeCatDeptoEmp.objects.filter( 
                Q(descri_largo_dep_emp__icontains = busqueda), 
                Q(estatus_depto__icontains = "A") 
            ).distinct()
    form = FormAdscripcion()  
    data = { 
        'entity' : listaAdscripcion,
        'paginator' : paginator,
        'FormAdscripcion' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionAdscripciones/GestionAdscripciones.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarAdscripciones(request, rowid_depto):
    try:
        ads = SeCatDeptoEmp.objects.get(rowid_depto=rowid_depto)
        ads.estatus_depto = "B"
    except SeCatDeptoEmp.DoesNotExist:
        raise Http404("La adscripcion no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "¡Adscripcion eliminada con exito!")
        ads.save()
        return redirect('vista_adscripciones')
    return render(request, "controlEscolar/catalogos/empleados/GestionAdscripciones/BorrarAdscripciones.html", {"Adscripcion": ads})
# Modifica un registro
@login_required
def vista_adscripciones_detail(request, rowid_depto):
    ads = SeCatDeptoEmp.objects.get(rowid_depto=rowid_depto)
    form = FormAdscripcion(instance=ads)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormAdscripcion(request.POST, instance = ads)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "¡Adscripcion actualizado con exito!")
            return redirect('vista_adscripciones') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionAdscripciones/ActualizarAdscripciones.html", {"Adscripcion" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/empleados/GestionAdscripciones/ActualizarAdscripciones.html", {"Adscripcion" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_adscripcion(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaAdscripcion=SeCatDeptoEmp.objects.filter(estatus_depto ="A") 
        data = {
            'count': listaAdscripcion.count(),
            'asc': listaAdscripcion
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionAdscripciones/ListaAdscripciones.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_adscripcion(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaAdscripcion=SeCatDeptoEmp.objects.filter(estatus_depto ="A")  
        data = {
            'count': listaAdscripcion.count(),
            'asc': listaAdscripcion
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionAdscripciones/ListaAdscripciones.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaAdscripciones.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_adscripcion (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaAdscripcion.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave', 'Consecutivo', 'Departamento', 'Abreviacion', 'Titular', 'Clave servicio', 'Estatus'])
    listaAdscripcion=SeCatDeptoEmp.objects.filter(estatus_depto ="A")  
    for asc in listaAdscripcion:
        writer.writerow([asc.id_depto, asc.conse_depto, asc.descri_largo_dep_emp, asc.descri_corto_dep_emp, asc.titular_depto, asc.clave_ser, asc.estatus_depto])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_adscripcion (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaAdscripcion.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Adscripcion')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave', 'Consecutivo', 'Departamento', 'Abreviacion', 'Titular', 'Clave servicio', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatDeptoEmp.objects.filter(estatus_depto="A").values_list('id_depto','conse_depto','descri_largo_dep_emp','descri_corto_dep_emp', 'titular_depto', 'clave_ser', 'estatus_depto')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################   Actididades   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaActididades(request):
    listaActividades = SeCatActividades.objects.filter(estatus_act="A").order_by('rowid_actividad')
    contador_id = listaActividades.count() 
    page = request.GET.get('page', 1)  
    try:  
        paginator = Paginator(listaActividades, 7)
        listaActividades = paginator.page(page)
    except: 
        raise Http404
    if request.method == 'POST': 
        form = FormActividades(request.POST) 
        if form.is_valid(): 
            act = form.save(commit=False)
            ultimo_id = SeCatActividades.objects.all().order_by('rowid_actividad').last() 
            act.rowid_actividad = ultimo_id.rowid_actividad + 1 
            act.save() 
            messages.success(request, "¡Actividad agregada con exito!")       
            return redirect('vista_actividades') 
        else: 
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionActividades/GestionActividades.html",{'entity' : listaActividades,'paginator' : paginator,'FormActividades' : form,'contador': contador_id})       
    elif request.method == 'GET': 
        busqueda = request.GET.get("search_actividad", None) 
        if busqueda: 
            listaActividades = SeCatActividades.objects.filter( 
                Q(descri_largo_act__icontains = busqueda), 
                Q(estatus_act__icontains = "A") 
            ).distinct()
    form = FormActividades()  
    data = { 
        'entity' : listaActividades,
        'paginator' : paginator,
        'FormActividades' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionActividades/GestionActividades.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarActididades(request, rowid_actividad):
    try:
        act = SeCatActividades.objects.get(rowid_actividad = rowid_actividad)
        act.estatus_act = "B"
    except SeCatActividades.DoesNotExist:
        raise Http404("La Actividad no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "¡Actividad eliminada con exito!")
        act.save()
        return redirect('vista_actividades')
    return render(request, "controlEscolar/catalogos/empleados/GestionActividades/BorrarActividades.html", {"Actividad": act})
# Modifica un registro
@login_required
def vista_actididades_detail(request, rowid_actividad):
    act = SeCatActividades.objects.get(rowid_actividad=rowid_actividad)
    form = FormActividades(instance=act)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormActividades(request.POST, instance = act)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "¡Actividad actualizada con exito!")
            return redirect('vista_actividades') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionActividades/ActualizarActividades.html", {"Actividad" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/empleados/GestionActividades/ActualizarActividades.html", {"Actividad" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_actididades(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaActividades=SeCatActividades.objects.filter(estatus_act ="A") 
        data = {
            'count': listaActividades.count(),
            'asc': listaActividades
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionActividades/ListaActividades.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_actididades(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaActividades=SeCatActividades.objects.filter(estatus_act ="A")  
        data = {
            'count': listaActividades.count(),
            'asc': listaActividades
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionActividades/ListaActividades.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaActividades.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_actididades (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaActividades.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave', 'Actividad', 'Abreviacion', 'Estatus'])
    listaActividades=SeCatActividades.objects.filter(estatus_act ="A")  
    for act in listaActividades:
        writer.writerow([act.id_actividad, act.descri_largo_act, act.descri_corto_act, act.estatus_act])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_actididades (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaActividades.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Actividades')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave', 'Actividad', 'Abreviacion', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatActividades.objects.filter(estatus_act="A").values_list('id_actividad','descri_largo_act','descri_corto_act','estatus_act')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response


##############################################   Instituciones   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaInstituciones(request):
    listaInstituciones = SeCatInstitucion.objects.filter(estatus_ins="A").order_by('rowid_institucion')
    contador_id = listaInstituciones.count() 
    page = request.GET.get('page', 1)  
    try:  
        paginator = Paginator(listaInstituciones, 7)
        listaInstituciones = paginator.page(page)
    except: 
        raise Http404
    if request.method == 'POST': 
        form = FormInstitucion(request.POST) 
        if form.is_valid(): 
            inst = form.save(commit=False)
            ultimo_id = SeCatInstitucion.objects.all().order_by('rowid_institucion').last() 
            inst.rowid_institucion = ultimo_id.rowid_institucion + 1 
            inst.save() 
            messages.success(request, "¡Institucion agregada con exito!")       
            return redirect('vista_instituciones') 
        else: 
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionInstituciones/GestionInstituciones.html",{'entity' : listaInstituciones,'paginator' : paginator,'form' : form,'contador': contador_id})       
    elif request.method == 'GET': 
        busqueda = request.GET.get("search_institucion", None) 
        if busqueda: 
            listaInstituciones = SeCatInstitucion.objects.filter( 
                Q(descri_largo_ins__icontains = busqueda), 
                Q(estatus_ins__icontains = "A") 
            ).distinct()
    form = FormInstitucion()  
    data = { 
        'entity' : listaInstituciones,
        'paginator' : paginator,
        'form' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionInstituciones/GestionInstituciones.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarInstituciones(request, rowid_institucion):
    try:
        inst = SeCatInstitucion.objects.get(rowid_institucion = rowid_institucion)
        inst.estatus_ins = "B"
    except SeCatInstitucion.DoesNotExist:
        raise Http404("La Institución no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "¡Institución eliminada con exito!")
        inst.save()
        return redirect('vista_instituciones')
    return render(request, "controlEscolar/catalogos/empleados/GestionInstituciones/BorrarInstituciones.html", {"Institucion": inst})
# Modifica un registro
@login_required
def vista_instituciones_detail(request, rowid_institucion):
    inst = SeCatInstitucion.objects.get(rowid_institucion = rowid_institucion)
    form = FormInstitucion(instance=inst)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormInstitucion(request.POST, instance = inst)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "¡Instituciónactualizada con exito!")
            return redirect('vista_instituciones') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionInstituciones/ActualizarInstituciones.html", {"form" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/empleados/GestionInstituciones/ActualizarInstituciones.html", {"form" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_instituciones(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaInstituciones = SeCatInstitucion.objects.filter(estatus_ins="A")
        data = {
            'count': listaInstituciones.count(),
            'instucion': listaInstituciones
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionInstituciones/ListaInstituciones.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_instituciones(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaInstituciones = SeCatInstitucion.objects.filter(estatus_ins="A")
        data = {
            'count': listaInstituciones.count(),
            'instucion': listaInstituciones
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionInstituciones/ListaInstituciones.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaInstituciones.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_instituciones (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaInstituciones.csv;'
    writer = csv.writer(response)
    writer.writerow(['Clave', 'Institucion', 'Abreviacion', 'Estatus'])
    listaInstituciones = SeCatInstitucion.objects.filter(estatus_ins="A")
    for inst in listaInstituciones:
        writer.writerow([inst.id_institucion, inst.descri_largo_ins, inst.descri_corto_ins, inst.estatus_ins])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_instituciones (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaInstituciones.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Instituciones')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Clave', 'Institucion', 'Abreviacion', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeCatInstitucion.objects.filter(estatus_ins="A").values_list('id_institucion','descri_largo_ins','descri_corto_ins','estatus_ins')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##############################################   EmpCar   #########################################################
#Agregar si es post y lista de todos / Aqui va la paguinacion
@login_required
def vistaEmpCar(request):
    listaEmpCar = SeTabEmpCar.objects.filter(estatus_inst="A").order_by('rowid_emp_car')
    contador_id = listaEmpCar.count() 
    page = request.GET.get('page', 1)  
    try:  
        paginator = Paginator(listaEmpCar, 7)
        listaEmpCar = paginator.page(page)
    except: 
        raise Http404
    if request.method == 'POST': 
        form = FormEmpCar(request.POST) 
        if form.is_valid(): 
            empcar = form.save(commit=False)
            ultimo_id = SeTabEmpCar.objects.all().order_by('rowid_emp_car').last() 
            empcar.rowid_emp_car = ultimo_id.rowid_emp_car + 1 
            empcar.save() 
            messages.success(request, "¡Empleado agregada con exito!")       
            return redirect('vista_EmpCars') 
        else: 
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionEmpCar/GestionEmpCar.html",{'entity' : listaEmpCar,'paginator' : paginator,'form' : form,'contador': contador_id})       
    elif request.method == 'GET': 
        busqueda = request.GET.get("search_empcar", None) 
        if busqueda: 
            listaEmpCar = SeTabEmpCar.objects.filter( 
                Q(descri_largo_car_emp__icontains = busqueda), 
                Q(estatus_inst__icontains = "A") 
            ).distinct()
    form = FormEmpCar()  
    data = { 
        'entity' : listaEmpCar,
        'paginator' : paginator,
        'form' : form,
        'contador': contador_id,
    }
    return render(request, "controlEscolar/catalogos/empleados/GestionEmpCar/GestionEmpCar.html",data)
# Elimina un registro que no elimina solo actualiza Status de A a B
@login_required
def eliminarEmpCar(request, rowid_emp_car):
    try:
        empcar = SeTabEmpCar.objects.get(rowid_emp_car = rowid_emp_car)
        empcar.estatus_inst = "B"
    except SeTabEmpCar.DoesNotExist:
        raise Http404("La Institución no existe")
    if request.method == 'POST': #Sobre escrive los valores
        messages.warning(request, "¡Carrera eliminada con exito!")
        empcar.save()
        return redirect('vista_EmpCars')
    return render(request, "controlEscolar/catalogos/empleados/GestionEmpCar/BorrarEmpCar.html", {"form": empcar})
# Modifica un registro
@login_required
def vista_EmpCar_detail(request, rowid_emp_car):
    empcar = SeTabEmpCar.objects.get(rowid_emp_car = rowid_emp_car)
    form = FormEmpCar(instance=empcar)
    if request.method == 'POST': #Sobre escrive los valores
        form = FormEmpCar(request.POST, instance = empcar)
        if form.is_valid():
            form.save()  #Guarda los cambios
            messages.info(request, "¡Emp Car actualizada con exito!")
            return redirect('vista_EmpCars') #retorna despues de actualizar
        else:
            messages.warning(request, "¡Alguno de los campos no es valido!") 
            return render(request, "controlEscolar/catalogos/empleados/GestionEmpCar/ActualizarEmpCar.html", {"form" : form})#envia al detalle con los campos no validos
    return render(request, "controlEscolar/catalogos/empleados/GestionEmpCar/ActualizarEmpCar.html", {"form" : form})#envia al detalle para actualizar
# primera de pdf posible imprimir / Funciona con la misma funcion en utils
class Export_print_EmpCar(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        listaEmpCar = SeTabEmpCar.objects.filter(estatus_inst="A")
        data = {
            'count': listaEmpCar.count(),
            'empcar': listaEmpCar
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionEmpCar/ListaEmpCar.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#Clase para crear Pdf / Funciona con la misma funcion en utils
class Export_pdf_EmpCar(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        listaEmpCar = SeTabEmpCar.objects.filter(estatus_inst="A")
        data = {
            'count': listaEmpCar.count(),
            'empcar': listaEmpCar
        }
        pdf = render_to_pdf('controlEscolar/catalogos/empleados/GestionEmpCar/ListaEmpCar.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'ListaEmpCar.pdf'
        content = "attachment; filename= %s" %(filename)
        response['Content-Disposition'] = content
        return response
# Exportar paises a CSV sin libreria 
@login_required
def export_csv_EmpCar (request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=ListaEmpCar.csv;'
    writer = csv.writer(response)
    writer.writerow(['Institucion', 'Nombre', 'Carrera','Abreviacion', 'Estatus'])
    listaEmpCar = SeTabEmpCar.objects.filter(estatus_inst="A")
    for e in listaEmpCar:
        writer.writerow([e.rowid_institucion.descri_largo_ins, e.rowid_empleado, e.descri_largo_car_emp, e.descri_corto_car_emp, e.estatus_inst])
    return response
# Exportar paises a xlwt sin con la libreria XLWT 
@login_required
def export_xlwt_EmpCar (request):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=ListaEmpCar.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('EmpCar')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.blod = True
    columns = ['Institucion', 'Nombre', 'Carrera','Abreviacion', 'Estatus']
    for col in range(len(columns)):
        ws.write(row_num,col,columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows=SeTabEmpCar.objects.filter(estatus_inst="A").values_list('rowid_institucion', 'rowid_empleado', 'descri_largo_car_emp','descri_corto_car_emp', 'estatus_inst')
    for row in rows:
        row_num+=1
        for col in range(len(row)):
            ws.write(row_num,col,str(row[col]), font_style)
    wb.save(response)
    return response

##################################################   Operaciones ####################################################

# Prueba
def listaEjemplo(request):
    form = FormsAspirantes()
    return render(request, "controlEscolar/operaciones/aspirantes/capturaAspirantes/capturaAspirantes.html",{'form': form})
