from django.urls import path
from . import views


urlpatterns = [
# CRUD PAISES
    #Vista maestra los registros con Status=A / Guarda los datos si es POST / Si es una peticion GET Busca los registros con el search / Manda los datos de la paguinacion
    path('vistaPaises/', views.vistaPaises, name="vistaPaises"), 
    # Actualiza el status de A a B / Elimina segun xD
    path('eliminarPais/<int:rowid_pais>/', views.eliminarPais, name="eliminar-pais"),
    # Actualiza los campos Nombre y abreviacion
    path('vistaPaises/<int:rowid_pais>/', views.vista_paises_detail, name="pais-detail"),
    # Exporta la lista de los paises en PDF
    path('export_pdf_paises/', views.Export_pdf_paises.as_view(), name="export-pdf-paises"),
    # Exporta la lista de los paises en CSV
    path('export_csv_paises/', views.export_csv_paises, name="export-csv-paises" ),
     # Exporta la lista de los paises en XLWT
    path('export_xlwt_paises/', views.export_xlwt_paises, name="export-xlwt-paises"),
    # Manda la pre-visualizacion para imprimir
    path('export_print_paises/', views.Export_print_paises.as_view(), name="export-print-paises"),
    # Vista de pre-visualizacion PFD solo para pruebas
    path('listaPaises/', views.listaPaises),
# CRUD Estados
    path('vistaEstados/', views.vistaEstados, name="vistaEstados"), 
    path('eliminarEstado/<int:rowid_edo>/', views.eliminarEstado, name="eliminar-estado"),
    path('vistaEstados/<int:rowid_edo>/', views.vista_estados_detail, name="estado-detail"),
    path('export_pdf_estados/', views.Export_pdf_estados.as_view(), name="export-pdf-estados"),
    path('export_csv_estados/', views.export_csv_estados, name="export-csv-estados" ),
    path('export_xlwt_estados/', views.export_xlwt_estados, name="export-xlwt-estados"),
    path('export_print_estados', views.Export_print_estados.as_view(), name="export-print-estados"),
    path('listaEstados/', views.listaEstados),
# CRUD MUNICIPIOS/DELEGACIONES
    path('vistaMunicipios/', views.vistaMunicipios, name="vistaMunicipios"), 
    path('eliminarMunicipio/<int:rowid_mundel>/', views.eliminarMunicipio, name="eliminar-municipio"),
    path('vistaMunicipios/<int:rowid_mundel>/', views.vista_municipios_detail, name="municipio-detail"), 
    path('export_pdf_municipios/', views.Export_pdf_municipios.as_view(), name="export-pdf-municipios"),
    path('export_csv_municipios/', views.export_csv_municipios, name="export-csv-municipios" ),
    path('export_xlwt_municipios/', views.export_xlwt_municipios, name="export-xlwt-municipios"),
    path('export_print_municipios', views.Export_print_municipios.as_view(), name="export-print-municipios"),
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

# ---------------------------------------------------------------------------------------------------------------------------------------------

#CRUD UNIVERSIDADES
    path('vistaUniversidades/', views.vistaUniversidades, name="vistaUniversidades"),
    path('eliminarUniversidad/<int:id_uni>/', views.eliminarUniversidad, name="eliminarUniversidad"),
    path('vistaUniversidades/<int:uni_id>/', views.vista_universidad_detail, name="universidad-detail"),
    path('export_pdf_universidades/', views.Export_pdf_universidades.as_view(), name="export-pdf-universidades"),
    path('export_print_universidades/', views.Export_print_universidades.as_view(), name="export-print-universidades"),
    path('export_csv_universidades/', views.export_csv_universidades, name="export-csv-universidades" ),
    path('export_xlwt_universidades/', views.export_xlwt_universidades, name="export-xlwt-universidades"),
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
 # CRUD AREA BACHILLERATO
    path('vistaAreaBachi/', views.vistaAreaBachi, name="vistaAreaBachi"), 
    path('eliminarAreaBachi/<int:id_area_bac>/', views.eliminarAreaBachi, name="eliminar-area-bachi"),
    path('vistaAreaBachi/<int:id_area_bac>/', views.vista_Area_Bac_detail, name="area-bachi-detail"),
    path('export_pdf_area_bachi/', views.Export_pdf_area_bachi.as_view(), name="export-pdf-area-bachi"),
    path('export_csv_area_bachi/', views.export_csv_area_bachi, name="export-csv-area-bachi" ),
    path('export_xlwt_area_bachi/', views.export_xlwt_areabachi, name="export-xlwt-area-bachi"),
    path('export_print_area_bac', views.Export_print_area_bac.as_view(), name="export-print-area-bac"),
# CRUD TIPO DE BAJAS
    path('vistaTipoBajas/', views.vistaTipoBajas, name="vistaTipoBajas"), 
    path('eliminarTipoBajas/<int:id_tipo_baj>/', views.eliminarTipoBajas, name="eliminar-tipo-bajas"),
    path('vistaTipoBajas/<int:id_tipo_baj>/', views.vista_tipobajas_detail, name="tipo-bajas-detail"),
    path('export_pdf_tipo_bajas/', views.Export_pdf_tipo_bajas.as_view(), name="export-pdf-tipo-bajas"),
    path('export_csv_tipo_bajas/', views.export_csv_tipo_bajas, name="export-csv-tipo-bajas" ),
    path('export_xlwt_tipo_bajas/', views.export_xlwt_tipo_bajas, name="export-xlwt-tipo-bajas"),
    path('export_print_tipo_baj', views.Export_print_tipobajas.as_view(), name="export-print-tipo-bajas"),
# CRUD Medios de difusion
    path('vistaMedios/', views.vistaMedios, name="vistaMedios"), 
    path('eliminarMedio/<int:id_medio_dif>/', views.eliminarMedio, name="eliminar-medio"),
    path('vistaMedios/<int:medio_id>/', views.vista_medios_detail, name="medio-detail"),
    path('export_pdf_medios/', views.Export_pdf_medios.as_view(), name="export-pdf-medios"),
    path('export_csv_medios/', views.export_csv_medios, name="export-csv-medios" ),
    path('export_xlwt_medios/', views.export_xlwt_medios, name="export-xlwt-medios"),
    path('export_print_medios', views.Export_print_medios.as_view(), name="export-print-medios"),
    path('listaMedios/', views.listaMedios),
# CRUD TIPO DE ESCUELA
    path('vistaEscuelas/', views.vistaEscuelas, name="vistaEscuelas"), 
    path('eliminarEscuela/<int:id_tipo_esc>/', views.eliminarEscuela, name="eliminar-escuela"),
    path('vistaEscuelas/<int:escuela_id>/', views.vista_escuelas_detail, name="escuela-detail"),
    path('Export_pdf_escuelas/', views.Export_pdf_escuelas.as_view(), name="export-pdf-escuelas"),
    path('export_csv_escuelas/', views.export_csv_escuelas, name="export-csv-escuelas" ),
    path('export_xlwt_escuelas/', views.export_xlwt_escuelas, name="export-xlwt-escuelas"),
    path('Export_print_escuelas', views.Export_print_escuelas.as_view(), name="export-print-escuelas"),
    path('listaEscuelas/', views.listaEscuelas),
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
]
