from django.urls import path
from . import views


urlpatterns = [
# -------------------------------------------- Direcciones --------------------------------------------- #
# CRUD PAISES
    #Vista maestra los registros con Status=A / Guarda los datos si es POST / Si es una peticion GET Busca los registros con el search / Manda los datos de la paguinacion
    path('vista-paises/', views.vistaPaises, name="vista_paises"), 
    # Actualiza el status de A a B / Elimina segun xD
    path('eliminar-pais/<int:rowid_pais>/', views.eliminarPais, name="eliminar_pais"),
    # Actualiza los campos Nombre y abreviacion
    path('vista-paises/<int:rowid_pais>/', views.vista_paises_detail, name="vista_pais"),
    # Exporta la lista de los paises en PDF
    path('export-pdf-paises/', views.Export_pdf_paises.as_view(), name="export_pdf_paises"),
    # Exporta la lista de los paises en CSV
    path('export-csv-paises/', views.export_csv_paises, name="export_csv_paises" ),
     # Exporta la lista de los paises en XLWT
    path('export-xlwt-paises/', views.export_xlwt_paises, name="export_xlwt_paises"),
    # Manda la pre-visualizacion para imprimir
    path('export-print-paises/', views.Export_print_paises.as_view(), name="export_print_paises"),
    # Vista de pre-visualizacion PFD solo para pruebas
    # path('listaPaises/', views.listaPaises),
# CRUD Estados
    path('vista-estados/', views.vistaEstados, name="vista_estados"), 
    path('eliminar-estado/<int:rowid_edo>/', views.eliminarEstado, name="eliminar_estado"),
    path('vista-estados/<int:rowid_edo>/', views.vista_estados_detail, name="vista_estado"),
    path('export-pdf-estados/', views.Export_pdf_estados.as_view(), name="export_pdf_estados"),
    path('export-csv-estados/', views.export_csv_estados, name="export_csv_estados" ),
    path('export-xlwt-estados/', views.export_xlwt_estados, name="export_xlwt_estados"),
    path('export-print-estados', views.Export_print_estados.as_view(), name="export_print_estados"),
    # path('listaEstados/', views.listaEstados),
# CRUD MUNICIPIOS/DELEGACIONES
    path('vista-municipios/', views.vistaMunicipios, name="vista_municipios"), 
    path('eliminar-municipio/<int:rowid_mundel>/', views.eliminarMunicipio, name="eliminar_municipio"),
    path('vista-municipio/<int:rowid_mundel>/', views.vista_municipios_detail, name="vista_municipio"), 
    path('export-pdf-municipios/', views.Export_pdf_municipios.as_view(), name="export_pdf_municipios"),
    path('export-csv-municipios/', views.export_csv_municipios, name="export_csv_municipios" ),
    path('export-xlwt-municipios/', views.export_xlwt_municipios, name="export_xlwt_municipios"),
    path('export-print-municipios', views.Export_print_municipios.as_view(), name="export_print_municipios"),
    path('listaMunicipios/', views.listaMunicipios),
# CRUD COLONIAS
    path('vistaColonias/', views.vistaColonias, name="vistaColonias"), 
    path('eliminarColonia/<int:rowid_col>/', views.eliminarColonia, name="eliminar-colonia"),
    path('vistaColonias/<int:rowid_col>/', views.vista_colonias_detail, name="colonia-detail"),
    path('export_pdf_colonias/', views.Export_pdf_colonias.as_view(), name="export-pdf-colonias"),
    path('export_csv_colonias/', views.export_csv_colonias, name="export-csv-colonias" ),
    path('export_xlwt_colonias/', views.export_xlwt_colonias, name="export-xlwt-colonias"),
    path('export_print_colonias', views.Export_print_colonias.as_view(), name="export-print-colonias"),
    path('listaColonias/', views.listaColonias),

# -------------------------------------------- Universidad --------------------------------------------- #

#CRUD UNIVERSIDADES
    path('vista-universidades/', views.vistaUniversidades, name="vista_universidades"),
    path('eliminar-universidad/<int:rowid_uni>/', views.eliminarUniversidad, name="eliminar-universidad"),
    path('vista-universidades/<int:rowid_uni>/', views.vista_universidad_detail, name="universidad_detail"),
    path('export-pdf-universidades/', views.Export_pdf_universidades.as_view(), name="export_pdf_universidades"),
    path('export-print-universidades/', views.Export_print_universidades.as_view(), name="export_print-universidades"),
    path('export-csv-universidades/', views.export_csv_universidades, name="export_csv_universidades" ),
    path('export-xlwt-universidades/', views.export_xlwt_universidades, name="export_xlwt_universidades"),

# CRUD DIVISIONES
    path('vista-Divisiones/', views.vista_Divisiones, name="vista_Divisiones"),
    path('eliminar-Divisiones/<int:rowid_div>/', views.eliminar_Divisiones, name="eliminar_Divisiones"),
    path('vista-Divisiones/<int:rowid_div>/', views.vista_divisiones_detail, name="division_detail"),
    path('export-pdf-divisiones/', views.Export_pdf_divisiones.as_view(), name="export_pdf_divisiones"),
    path('export-csv-divisiones/', views.export_csv_divisiones, name="export_csv_divisiones" ),
    path('export-xlwt-divisiones/', views.export_xlwt_divisiones, name="export_xlwt_divisiones"),
    path('export-print-divisiones/', views.Export_print_divisiones.as_view(), name="export_print_divisiones"),

#CRUD CARRERAS
    path('vista-carreras/', views.vistaCarreras, name="vista_carreras"),
    path('eliminar-carreras/<int:rowid_car>', views.eliminarCarreras, name="eliminar_carreras"),
    path('vista-carreras/<int:rowid_car>', views.vista_carreras_detail, name="carrera_detail"),
    path('export-print-carreras', views.Export_print_carreras.as_view(), name="export_print_carreras"),
    path('export-pdf-carreras/', views.Export_pdf_carreras.as_view(), name="export_pdf_carreras"),
    path('export-csv-carreras/', views.export_csv_carreras, name="export_csv_carreras"),
    path('export-xlwt-carreras/', views.export_xlwt_carreras, name="export_xlwt_carreras"),

# CRUD Periodos
    path('vista-periodos', views.vistaPeriodos, name="vista_periodos"),
    path('eliminar-periodo/<int:rowid_per>', views.eliminarPeriodo, name="eliminar_periodo"),
    path('vista-periodos/<int:rowid_per>/', views.vista_periodos_detail, name="periodos_detail"),
    path('export-print-periodos/', views.Export_print_periodos.as_view(), name="export_print_periodos"),
    path('export-pdf-periodos/', views.Export_pdf_periodos.as_view(), name="export_pdf_periodos"),
    path('export-csv-periodos/', views.export_csv_periodos, name="export_csv_periodos"),
    path('export-xlwt-periodos/', views.export_xlwt_periodos, name="export_xlwt_periodos"),

# -------------------------------------------- Aspirantes --------------------------------------------- #

# CRUD MEDIO DE DIFUSION
    path('vista-Medios/', views.vista_Medios, name="vista_Medios"), 
    path('eliminar-Medio/<int:rowid_medio_dif>/', views.eliminar_Medio, name="eliminar_medio"),
    path('vista-Medios/<int:rowid_medio_dif>/', views.vista_medios_detail, name="medio_detail"),
    path('export-pdf-medios/', views.Export_pdf_medios.as_view(), name="export_pdf_medios"),
    path('export-csv-medios/', views.export_csv_medios, name="export_csv_medios" ),
    path('export-xlwt-medios/', views.export_xlwt_medios, name="export_xlwt_medios"),
    path('export-print-medios', views.Export_print_medios.as_view(), name="export_print_medios"),
# CRUD TIPO DE ESCUELA
    path('vista-Escuelas/', views.vista_Escuelas, name="vista_Escuelas"), 
    path('eliminar-Escuela/<int:rowid_tipo_esc>/', views.eliminar_Escuela, name="eliminar_escuela"),
    path('vista-Escuelas/<int:rowid_tipo_esc>/', views.vista_escuelas_detail, name="escuela_detail"),
    path('Export-pdf-escuelas/', views.Export_pdf_escuelas.as_view(), name="export_pdf_escuelas"),
    path('export-csv-escuelas/', views.export_csv_escuelas, name="export_csv_escuelas" ),
    path('export-xlwt-escuelas/', views.export_xlwt_escuelas, name="export_xlwt_escuelas"),
    path('Export-print-escuelas', views.Export_print_escuelas.as_view(), name="export_print_escuelas"),
 # CRUD AREA BACHILLERATO
    path('vista-AreaBachi/', views.vista_AreaBachi, name="vista_AreaBachi"), 
    path('eliminar-AreaBachi/<int:rowid_area_bac>/', views.eliminar_AreaBachi, name="eliminar_areabachi"),
    path('vista-AreaBachi/<int:rowid_area_bac>/', views.vista_AreaBachi_detail, name="areabachi_detail"),
    path('export-pdf-areabachi/', views.Export_pdf_areabachi.as_view(), name="export_pdf_areabachi"),
    path('export-csv-areabachi/', views.export_csv_areabachi, name="export_csv_areabachi" ),
    path('export-xlwt_areabachi/', views.export_xlwt_areabachi, name="export_xlwt_areabachi"),
    path('export-print-areabachi', views.Export_print_areabachi.as_view(), name="export_print_areabachi"),
    # CRUD INDICADORES ASPIRANTES
    path('vista-IndAsp/', views.vista_IndAsp, name="vista_IndAsp"),
    path('eliminar-IndAsp/<int:rowid_pro_ind_asp>/', views.eliminar_IndAsp, name="eliminar_IndAsp"),
    path('vista-IndAsp/<int:rowid_pro_ind_asp>/', views.vista_IndAsp_detail, name="IndAsp_detail"),
    path('export-pdf-IndAsp/', views.Export_pdf_IndAsp.as_view(), name="export_pdf_IndAsp"),
    path('export-csv-IndAsp/', views.export_csv_IndAsp, name="export_csv_IndAsp" ),
    path('export-xlwt-IndAsp/', views.export_xlwt_IndAsp, name="export_xlwt_IndAsp"),
    path('export-print-IndAsp', views.Export_print_IndAsp.as_view(), name="export_print_IndAsp"),





# CRUD Nivel Academico
    path('vistaNivelAca/', views.vistaNivelAca, name="vistaNivelAca"),
    path('eliminarNivelAca/<int:id_academico>/', views.eliminarNivelAca, name="eliminarNivelAca"),
    path('vistaNivelAca/<int:aca_id>/', views.vista_nivel_aca_detail, name="academico-detail"),
    path('export_print_nivel_academico/', views.Export_print_nivel_academico.as_view(), name="export-print-nivel-academico"),
    path('export_pdf_nivel_academico/', views.Export_pdf_nivel_academico.as_view(), name="export-pdf-nivel-academico"),
    path('export_csv_nivel_academico/', views.export_csv_nivel_academico, name="export-csv-nivel-academico"),
    path('export_xlwt_nivel_academico/', views.export_xlwt_nivel_academico, name="export-xlwt-nivel-academico"),
# CRUD Plazas
    path('vistaPlaza/', views.vistaPlaza, name="vistaPlaza"),
    path('eliminarPlaza/<int:id_plaza>/', views.eliminarPlaza, name="eliminarPlaza"),
    path('vistaPlaza/<int:plaza_id>/', views.vista_plaza_detail, name="plaza-detail"),
    path('export_print_plaza/', views.Export_print_plaza.as_view(), name="export-print-plaza"),
    path('export_pdf_plaza/', views.Export_pdf_plaza.as_view(), name="export-pdf-plaza"),
    path('export_csv_plaza/', views.export_csv_plaza, name="export-csv-plaza"),
    path('export_xlwt_plaza/', views.export_xlwt_plaza, name="export-xlwt-plaza"),

# CRUD TIPO DE BAJAS
    path('vistaTipoBajas/', views.vistaTipoBajas, name="vistaTipoBajas"), 
    path('eliminarTipoBajas/<int:id_tipo_baj>/', views.eliminarTipoBajas, name="eliminar-tipo-bajas"),
    path('vistaTipoBajas/<int:id_tipo_baj>/', views.vista_tipobajas_detail, name="tipo-bajas-detail"),
    path('export_pdf_tipo_bajas/', views.Export_pdf_tipo_bajas.as_view(), name="export-pdf-tipo-bajas"),
    path('export_csv_tipo_bajas/', views.export_csv_tipo_bajas, name="export-csv-tipo-bajas" ),
    path('export_xlwt_tipo_bajas/', views.export_xlwt_tipo_bajas, name="export-xlwt-tipo-bajas"),
    path('export_print_tipo_baj', views.Export_print_tipobajas.as_view(), name="export-print-tipo-bajas"),
# CRUD BECAS
    path('vistaBecas/', views.vistaBecas, name="vistaBecas"), 
    path('eliminarBeca/<int:id_becas>/', views.eliminarBeca, name="eliminar-beca"),
    path('vistaBecas/<int:beca_id>/', views.vista_becas_detail, name="beca-detail"),
    path('Export_pdf_becas/', views.Export_pdf_becas.as_view(), name="export-pdf-becas"),
    path('export_csv_becas/', views.export_csv_becas, name="export-csv-becas" ),
    path('export_xlwt_becas/', views.export_xlwt_becas, name="export-xlwt-becas"),
    path('Export_print_becas', views.Export_print_becas.as_view(), name="export-print-becas"),
    path('listaBecas/', views.listaBecas),
# CRUD TIPO DE CAMBIOS
    path('vistaCambios/', views.vistaCambios, name="vistaCambios"), 
    path('eliminarCambio/<int:id_tipo_cambio>/', views.eliminarCambio, name="eliminar-cambio"),
    path('vistaCambios/<int:cambio_id>/', views.vista_cambios_detail, name="cambio-detail"),
    path('Export_pdf_cambios/', views.Export_pdf_cambios.as_view(), name="export-pdf-cambios"),
    path('export_csv_cambios/', views.export_csv_cambios, name="export-csv-cambios" ),
    path('export_xlwt_cambios/', views.export_xlwt_cambios, name="export-xlwt-cambios"),
    path('Export_print_cambios', views.Export_print_cambios.as_view(), name="export-print-cambios"),
    path('listaCambios/', views.listaCambios),
# CRUD Plan de Estudio 
    path('vistaPlanE/', views.vistaPlanE, name="vistaPlaneEstudios"),
    path('eliminarPlan/<int:id_plan_est>/', views.eliminarPlan, name="eliminar-plan"),
    path('vistaPlanE/<int:plan_est_id>/', views.vista_planE_detail, name="vista_planE_detail"), 
    path('export_pdf_planes/', views.Export_pdf_planE.as_view(), name="export-pdf-planes"),
    path('export_csv_planes/', views.export_csv_planE, name="export-csv-planes" ),
    path('export_xlwt_planes/', views.export_xlwt_plan, name="export-xlwt-planes"),
    path('export_print_plan', views.Export_print_planE.as_view(), name="export-print-plan"),
# CRUD INDICADORES
    path('vistaIndicador/', views.vistaIndicador, name="VistaIndicadores"),
    path('eliminarIndicador/<int:id_indicador>/', views.eliminarIndicador, name="eliminar-indi"),
    path('vistaIndicador/<int:id_indicador>/', views.vista_indicador_detail, name="vista_indicadores_detail"),
    path('export_pdf_ind/', views.Export_print_ind.as_view(), name="export-print-indicadores"),
    path('export_pdf_indicador/', views.Export_pdf_indi.as_view(), name="export-pdf-indicadores"),
    path('export_csv_indi/', views.export_csv_indi, name="export-csv-indicadores" ),
    path('export_xlwt_indicador/', views.export_xlwt_indicador, name="export-xlwt-indicadores"),
# CRUD GRADOS
    path('vistaGrados/', views.vistaGrados, name="vistaGrados"),
    path('eliminarGrado/<int:id_grado>/', views.eliminarGrado, name="eliminar-grado"),
    path('vistaGrados/<int:grado_id>/', views.vista_grados_detail, name="vista_grados_detail"),
    path('export_pdf_grados/', views.Export_print_grados.as_view(), name="export-print-grados"),
    path('export_pdf_grado/', views.Export_pdf_grado.as_view(), name="export-pdf-grado"),
    path('export_csv_grados/', views.export_csv_grados, name="export-csv-grados" ),
    path('export_xlwt_grados/', views.export_xlwt_grados, name="export-xlwt-grados"),


# Registro Aspirantes
    path('listaEjemplo/', views.listaEjemplo),


# CRUD Adscripcion
    path('vista-adscripciones/', views.vistaAdscripciones, name="vista_adscripciones"), 
    path('eliminar-adscripcion/<int:rowid_depto>/', views.eliminarAdscripciones, name="eliminar_adscripcion"),
    path('vista-adscripcion/<int:rowid_depto>/', views.vista_adscripciones_detail, name="vista_adscripcion"),
    path('export-pdf-adscripcion/', views.Export_pdf_adscripcion.as_view(), name="export_pdf_adscripcion"),
    path('export-csv-adscripcion/', views.export_csv_adscripcion, name="export_csv_adscripcion" ),
    path('export-xlwt-adscripcion/', views.export_xlwt_adscripcion, name="export_xlwt_adscripcion"),
    path('export-print-adscripcion/', views.Export_print_adscripcion.as_view(), name="export_print_adscripcion"),
# CRUD Actividades 
    path('vista-actividades/', views.vistaActididades, name="vista_actividades"), 
    path('eliminar-actividades/<int:rowid_actividad>/', views.eliminarActididades, name="eliminar_actividades"),
    path('vista-actividades/<int:rowid_actividad>/', views.vista_actididades_detail, name="vista_actividades"),
    path('export-pdf-actividades/', views.Export_pdf_actididades.as_view(), name="export_pdf_actividades"),
    path('export-csv-actividades/', views.export_csv_actididades, name="export_csv_actividades"),
    path('export-xlwt-actividades/', views.export_xlwt_actididades, name="export_xlwt_actividades"),
    path('export-print-actividades/', views.Export_print_actididades.as_view(), name="export_print_actividades"),
# CRUD Instituciones
    path('vista-instituciones/', views.vistaInstituciones, name="vista_instituciones"), 
    path('eliminar-instituciones/<int:rowid_institucion>/', views.eliminarInstituciones, name="eliminar_instituciones"),
    path('vista-instituciones/<int:rowid_institucion>/', views.vista_instituciones_detail, name="vista_instituciones"),
    path('export-pdf-instituciones/', views.Export_pdf_instituciones.as_view(), name="export_pdf_instituciones"),
    path('export-csv-instituciones/', views.export_csv_instituciones, name="export_csv_instituciones"),
    path('export-xlwt-instituciones/', views.export_xlwt_instituciones, name="export_xlwt_instituciones"),
    path('export-print-instituciones/', views.Export_print_instituciones.as_view(), name="export_print_instituciones"),
# CRUD EmpCar
    path('vista-EmpCars/', views.vistaEmpCar, name="vista_EmpCars"), 
    path('eliminar-EmpCar/<int:rowid_emp_car>/', views.eliminarEmpCar, name="eliminar_EmpCar"),
    path('vista-EmpCar/<int:rowid_emp_car>/', views.vista_EmpCar_detail, name="vista_EmpCar"),
    path('export-pdf-EmpCar/', views.Export_pdf_EmpCar.as_view(), name="export_pdf_EmpCar"),
    path('export-csv-EmpCar/', views.export_csv_EmpCar, name="export_csv_EmpCar"),
    path('export-xlwt-EmpCar/', views.export_xlwt_EmpCar, name="export_xlwt_EmpCar"),
    path('export-print-EmpCar/', views.Export_print_EmpCar.as_view(), name="export_print_EmpCar"),
]
