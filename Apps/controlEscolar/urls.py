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
# CRUD ASENTAMIENTO
    path('vista-asen/', views.vistaAsen, name="vista_asen"),
    path('eliminar-asen/<int:rowid_asentamiento>/', views.eliminarAsen, name="eliminar_asen"),
    path('vista-asen/<int:rowid_asentamiento>/', views.vista_asen_detail, name="vista_asen"),
    path('export-pdf-asen/', views.Export_pdf_asen.as_view(), name="export_pdf_asen"),
    path('export-csv-asen/', views.export_csv_asen, name="export_csv_asen"),
    path('export-xlwt-asen/', views.export_xlwt_asen, name="export_xlwt_asen"),
    path('export-print-asen/', views.Export_print_asen.as_view(), name="export_print_asen"),
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

# -------------------------------------------- Plan de Estudios  --------------------------------------------- #

# CRUD PLAN DE ESTUDIO
    path('vista-PlanE/', views.vistaPlanE, name="vista_Plan_Estudios"),
    path('eliminar-Plan/<int:rowid_plan_est>/', views.eliminarPlan, name="eliminar_plan"),
    path('vistaPlanE/<int:rowid_plan_est>/', views.vista_planE_detail, name="vista_planE_detail"), 
    path('export-pdf-planes/', views.Export_pdf_planE.as_view(), name="export_pdf_planes"),
    path('export-csv-planes/', views.export_csv_planE, name="export_csv_planes" ),
    path('export-xlwt-planes/', views.export_xlwt_plan, name="export_xlwt_planes"),
    path('export-print-plan', views.Export_print_planE.as_view(), name="export_print_plan"),
# CRUD ASIGNATURA
    path('vista-asignatura/', views.vistaAsi, name="vista_asignatura"),
    path('eliminar_asignatura/<int:rowid_asignatura>/', views.eliminarAsignatura),
    path('vista_asignatura/<str:rowid_asignatura>/', views.vista_asig_detail),
    path('export-print-asig/', views.Export_print_asi.as_view(), name="export_print_asignatura"),
    path('export-pdf-asig/', views.Export_pdf_asi.as_view(), name="export_pdf_asignatura"),
    path('export-csv-asig/', views.export_csv_asi, name="export_csv_asignatura" ),
    path('export-xlwt-asig/', views.export_xlwt_asi, name="export_xlwt_asignatura"),
# CRUD INDICADORES
    path('vista-indicador/', views.vistaIndicador, name="Vista_indicadores"),
    path('eliminar-indicador/<int:rowid_indicador>/', views.eliminarIndicador, name="eliminar_indi"),
    path('vista-indicador/<int:rowid_indicador>/', views.vista_indicador_detail, name="vista_indicadores_detail"),
    path('export-print-ind/', views.Export_print_ind.as_view(), name="export_print_indicadores"),
    path('export-pdf-indicador/', views.Export_pdf_indi.as_view(), name="export_pdf_indicadores"),
    path('export-csv-indi/', views.export_csv_indi, name="export_csv_indicadores" ),
    path('export-xlwt-indicador/', views.export_xlwt_indicador, name="export_xlwt_indicadores"),
# CRUD PLAN DE ESTUDIO ASIGNATURA
    path('vista-pea/', views.vistaPea, name="vista_pea"),
    path('eliminar-pea/<str:rowid_pro_plan_est>', views.eliminarPea, name="eliminar_pea"),
    path('vista-pea/<str:rowid_pro_plan_est>', views.vista_pea_detail, name="vista_pea_detail"),
    path('export-print-pea/', views.Export_print_pea.as_view(), name="export_print_pea"),
    path('export-pdf-pea/', views.Export_pdf_pea.as_view(), name="export_pdf_pea"),
    path('export-csv-pea/', views.export_csv_pea, name="export_csv_pea" ),
    path('export-xlwt-pea/', views.export_xlwt_pea, name="export_xlwt_pea"),
# CRUD PLAN DE ESTUDIO ASIGNATURA INDICADOR
    path('vista-planEAI/', views.vistaPlanEAI, name="vista_planEAI"),
    path('eliminar-peai/<int:rowid_pro_asi_ind>/', views.eliminarPeai, name="eliminar-peai"),
    path('vista-planEAI/<int:rowid_pro_asi_ind>/', views.vista_peai_detail, name="vista_peai_detail"),
    path('export-print-peai/', views.Export_print_peai.as_view(), name="export_print_peai"),
    path('export-pdf-peai/', views.Export_pdf_peai.as_view(), name="export_pdf_peai"),
    path('export-csv-peai/', views.export_csv_peai, name="export_csv_peai" ),
    path('export-xlwt-peai/', views.export_xlwt_peai, name="export_xlwt_peai"),

# -------------------------------------------- Aspirantes --------------------------------------------- #

# CRUD Escuela de Procedencia
    path('vista-escpro/', views.vistaEscProc, name="vista_escpro"),
    path('eliminar-escpro/<int:rowid_esc_proc>/', views.eliminarEscProc, name="eliminar_escpro"),
    path('vista-escpro/<int:rowid_esc_proc>/', views.vista_escpro_detail, name="vista_escpro"),
    path('export-pdf-escpro/', views.Export_pdf_escpro.as_view(), name="export_pdf_escpro"),
    path('export-csv-escpro/', views.export_csv_escpro, name="export_csv_escpro"),
    path('export-xlwt-escpro/', views.export_xlwt_escpro, name="export_xlwt_escpro"),
    path('export-print-escpro/', views.Export_print_escpro.as_view(), name="export_print_escpro"),
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

# -------------------------------------------- Estudiantes --------------------------------------------- #

# CRUD Estudiante
    path('vista-estudiante/', views.vistaEstudiante, name="vista_estudiante"),
    path('eliminar-estudiante/<int:rowid_matricula>/', views.eliminarEstudiante, name="eliminar_estu"),
    path('vista-estudiante/<int:rowid_matricula>/', views.vista_estudiante_detail, name="estu_detail"),
    path('export-print-estudiante/', views.Export_print_estudiante.as_view(), name="export_print_estudiante"),
    path('export-pdf-estudiante/', views.Export_pdf_estudiante.as_view(), name="export_pdf_estudiante"),
    path('export-csv-estudiante/', views.export_csv_estudiante, name="export_csv_estudiante" ),
    path('export-xlwt-estudiante/', views.export_xlwt_estudiante, name="export_xlwt_estudiante"),
# CRUD DOCUMENTACION
    path('vista-Documentacion/', views.vista_Documentacion, name="vista_Documentacion"),
    path('eliminar-Documentacion/<int:rowid_doc>/', views.eliminar_Documentacion, name="eliminar_Documentacion"),
    path('vista-Documentacion/<int:rowid_doc>/', views.vista_Documentacion_detail, name="Documentacion_detail"),
    path('export-print-Documentacion/', views.Export_print_Documentacion.as_view(), name="export_print_Documentacion"),
    path('export-pdf-Documentacion/', views.Export_pdf_Documentacion.as_view(), name="export_pdf_Documentacion"),
    path('export-csv-Documentacion/', views.export_csv_Documentacion, name="export_csv_Documentacion" ),
    path('export-xlwt-Documentacion/', views.export_xlwt_Documentacion, name="export_xlwt_Documentacion"),
# # CRUD GRUPO
    path('vista-Grupo/', views.vista_Grupo, name="vista_Grupo"),
    path('eliminar-Grupo/<int:rowid_grupo>/', views.eliminar_Grupo, name="eliminar_grupo"),
    path('vista-Grupo/<int:rowid_grupo>/', views.vista_grupo_detail, name="Grupo_detail"),
    path('export-pdf-grupos/', views.Export_print_grupos.as_view(), name="export_print_grupos"),
    path('export-pdf-grupo/', views.Export_pdf_grupo.as_view(), name="export_pdf_grupo"),
    path('export-csv-grupos/', views.export_csv_grupos, name="export_csv_grupos" ),
    path('export-xlwt-grupos/', views.export_xlwt_grupos, name="export_xlwt_grupos"),
# CRUD ESTATUS-ESTUDIANTE
    path('vista-Estatus/', views.vista_Estatus, name="vista_Estatus"),
    path('eliminar-Estatus/<int:rowid_evento_est>/', views.eliminar_Estatus, name="eliminar_estatus"),
    path('vista-Estatus/<int:rowid_evento_est>/', views.vista_Estatus_detail, name="estatus_detail"),
    path('export-print-estatus/', views.Export_print_estatus.as_view(), name="export_print_estatus"),
    path('export-pdf-estatus/', views.Export_pdf_estatus.as_view(), name="export_pdf_estatus"),
    path('export-csv-esttatus/', views.export_csv_estatus, name="export_csv_estatus" ),
    path('export-xlwt-estatus/', views.export_xlwt_estatus, name="export_xlwt_estatus"),
# CRUD GRADOS
    path('vista-Grados/', views.vista_Grados, name="vista_Grados"),
    path('eliminar-Grado/<int:rowid_grado>/', views.eliminar_Grado, name="eliminar_grado"),
    path('vista-Grados/<int:rowid_grado>/', views.vista_grados_detail, name="grados_detail"),
    path('export-pdf-grados/', views.Export_print_grados.as_view(), name="export_print_grados"),
    path('export-pdf-grado/', views.Export_pdf_grado.as_view(), name="export_pdf_grado"),
    path('export-csv-grados/', views.export_csv_grados, name="export_csv_grados" ),
    path('export-xlwt-grados/', views.export_xlwt_grados, name="export_xlwt_grados"),
# CRUD SALONES
    path('vista-Salones/', views.vista_Salones, name="vista_Salones"), 
    path('eliminar-Salones/<int:rowid_salon>/', views.eliminar_Salones, name="eliminar_salones"),
    path('vista-Salones/<int:rowid_salon>/', views.vista_salones_detail, name="salones_detail"),
    path('export-pdf-salones/', views.Export_pdf_salones.as_view(), name="export_pdf_salones"),
    path('export-csv-salones/', views.export_csv_salones, name="export_csv_salones" ),
    path('export-xlwt-salones/', views.export_xlwt_salones, name="export_xlwt_salones"),
    path('export-print-salones', views.Export_print_salones.as_view(), name="export_print_salones"),
# CRUD BECAS
    path('vista-Becas/', views.vista_Becas, name="vista_Becas"), 
    path('eliminar-Beca/<int:rowid_becas>/', views.eliminar_Beca, name="eliminar_beca"),
    path('vista-Becas/<int:rowid_becas>/', views.vista_becas_detail, name="beca_detail"),
    path('Export-pdf-becas/', views.Export_pdf_becas.as_view(), name="export_pdf_becas"),
    path('export-csv-becas/', views.export_csv_becas, name="export_csv_becas" ),
    path('export-xlwt-becas/', views.export_xlwt_becas, name="export_xlwt_becas"),
    path('Export-print-becas', views.Export_print_becas.as_view(), name="export_print_becas"),
# CRUD TIPO DE CAMBIOS
    path('vista-Cambios/', views.vista_Cambios, name="vista_Cambios"), 
    path('eliminar-Cambio/<int:rowid_tipo_cambio>/', views.eliminar_Cambio, name="eliminar_cambio"),
    path('vista-Cambios/<int:rowid_tipo_cambio>/', views.vista_cambios_detail, name="cambio_detail"),
    path('Export-pdf-cambios/', views.Export_pdf_cambios.as_view(), name="export_pdf_cambios"),
    path('export-csv-cambios/', views.export_csv_cambios, name="export_csv_cambios" ),
    path('export-xlwt-cambios/', views.export_xlwt_cambios, name="export_xlwt_cambios"),
    path('Export-print-cambios', views.Export_print_cambios.as_view(), name="export_print_cambios"),
# CRUD TIPO DE BAJAS
    path('vista-TipoBajas/', views.vista_TipoBajas, name="vista_TipoBajas"), 
    path('eliminar-TipoBajas/<int:rowid_tipo_baj>/', views.eliminar_TipoBajas, name="eliminar_tipobajas"),
    path('vista-TipoBajas/<int:rowid_tipo_baj>/', views.vista_tipobajas_detail, name="tipobajas_detail"),
    path('export-pdf-tipobajas/', views.Export_pdf_tipobajas.as_view(), name="export_pdf_tipobajas"),
    path('export-csv-tipobajas/', views.export_csv_tipobajas, name="export_csv_tipobajas" ),
    path('export-xlwt-tipobajas/', views.export_xlwt_tipobajas, name="export_xlwt_tipobajas"),
    path('export-print-tipobajas', views.Export_print_tipobajas.as_view(), name="export_print_tipobajas"),

# -------------------------------------------- Empleados --------------------------------------------- #

# CRUD Empleado
    path('vista-emp/', views.vistaEmpleados, name="vista_emp"),
    path('eliminar-emp/<int:rowid_empleado>/', views.eliminarEmpleado, name="eliminar_empleado"),
    path('vista-emp/<int:rowid_empleado>/', views.vista_emp_detail, name="emp-detail"),
    path('export-print-emp/', views.Export_print_emp.as_view(), name="export_print_emp"),
    path('export-pdf-emp/', views.Export_pdf_emp.as_view(), name="export_pdf_emp"),
    path('export-csv-emp/', views.export_csv_emp, name="export_csv_emp"),
    path('export-xlwt-emp/', views.export_xlwt_emp, name="export_xlwt_emp"),
# CRUD Nivel Academico
    path('vista-nivelaca/', views.vistaNivelAca, name="vista_nivelaca"),
    path('eliminar-nivelaca/<int:rowid_academico>/', views.eliminarNivelAca, name="eliminar_nivelaca"),
    path('vista-nivelaca/<int:rowid_academico>/', views.vista_nivel_aca_detail, name="academico_detail"),
    path('export-print-nivel-academico/', views.Export_print_nivel_academico.as_view(), name="export_print_nivel_academico"),
    path('export-pdf-nivel-academico/', views.Export_pdf_nivel_academico.as_view(), name="export_pdf_nivel_academico"),
    path('export-csv-nivel-academico/', views.export_csv_nivel_academico, name="export_csv_nivel_academico"),
    path('export-xlwt-nivel-academico/', views.export_xlwt_nivel_academico, name="export_xlwt_nivel_academico"),
# CRUD Plazas
    path('vista-plaza/', views.vistaPlaza, name="vista_plaza"),
    path('eliminar-plaza/<int:rowid_plaza>/', views.eliminarPlaza, name="eliminar_plaza"),
    path('vista-plaza/<int:rowid_plaza>/', views.vista_plaza_detail, name="plaza_detail"),
    path('export-print-plaza/', views.Export_print_plaza.as_view(), name="export_print_plaza"),
    path('export-pdf-plaza/', views.Export_pdf_plaza.as_view(), name="export_pdf_plaza"),
    path('export-csv-plaza/', views.export_csv_plaza, name="export_csv_plaza"),
    path('export-xlwt-plaza/', views.export_xlwt_plaza, name="export_xlwt_plaza"),
# CRUD Tipo Puesto
    path('vista-tipopue/', views.vistaTipoPue, name="vista_tipopue"),
    path('eliminar-tipopue/<int:rowid_puesto>/', views.eliminarTipoPue, name="eliminar_tipopue"),
    path('vista-tipopue/<int:rowid_puesto>/', views.vista_tipopue_detail, name="tipopue-detail"),
    path('export-print-tipopue/', views.Export_print_tipopue.as_view(), name="export_print_tipopue"),
    path('export-pdf-tipopue/', views.Export_pdf_tipopue.as_view(), name="export_pdf_tipopue"),
    path('export-csv-tipopue/', views.export_csv_tipopue, name="export_csv_tipopue"),
    path('export-xlwt-tipopue/', views.export_xlwt_tipopue, name="export_xlwt_tipopue"),
# CRUD Sueldo
    path('vista-su/', views.vistaSueldos, name="vista_su"),
    path('eliminar-su/<int:rowid_sueldo>/', views.eliminarSueldos, name="eliminar_su"),
    path('vista-su/<int:rowid_sueldo>/', views.vista_su_detail, name="su-detail"),
    path('export-print-su/', views.Export_print_su.as_view(), name="export_print_su"),
    path('export-pdf-su/', views.Export_pdf_su.as_view(), name="export_pdf_su"),
    path('export-csv-su/', views.export_csv_su, name="export_csv_su"),
    path('export-xlwt-su/', views.export_xlwt_su, name="export_xlwt_su"),
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

# -------------------------------------------- Operaciones --------------------------------------------- #

# Registro Aspirantes
    path('listaEjemplo/', views.listaEjemplo),

]