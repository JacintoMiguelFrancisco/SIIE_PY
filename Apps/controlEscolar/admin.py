from django.contrib import admin

# Import - export
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#Models
from .models import (
    SeCatPais, SeCatEstado, SeCatMunicipioDelegacion, SeCatAsentamiento, SeCatColonia,  # Direcciones
    SeCatUniversidad, SeCatDivision, SeCatCarrera, SeCatPeriodos, # Universidades
    SeCatEscuelaProcedencia, SeCatMedioDifusion, SeCatTipoEscuela, SeCatAreaBachillerato, SeProIndAsp, # Aspirantes
    SeTabEstudiante, SeCatDocumentacion,SeCatGrupo,SeCatEstatusEstudiante, SeCatGrado, SeCatSalones, SeCatTipoBajas, SeCatBecas, SeCatTipoCambio, # Estudintes
    SeCatEmpleado, SeCatNivelAcademico, SeCatPlaza, SeCatTipoPuesto, SeCatSueldos, SeCatDeptoEmp, SeCatActividades, SeCatInstitucion, SeTabEmpCar, # Empleados
    SeCatPlaEstudio, SeCatAsignatura, SeCatIndicador, SeProPlanEstudio, SeProAsiIndicador, # Plan de Estudio
    SeTabAspirante, SeProAspDocu, SeTabAceptados, # Aspirante
)
# -------------------------------------------- Direcciones --------------------------------------------- #

##################### Admin de Paises  ################# 
class PaisResources(resources.ModelResource):
    fields = ('rowid_pais','id_pais', 'descri_largo_pais', 'descri_corto_pais', 'estatus_pais')
    class Meta:
        model = SeCatPais
@admin.register(SeCatPais)
class PaisAdmin(ImportExportModelAdmin):
    resources_class = PaisResources
    list_display = ('rowid_pais','id_pais', 'descri_largo_pais', 'descri_corto_pais', 'estatus_pais')
    search_fields = ['rowid_pais','id_pais', 'descri_largo_pais', 'descri_corto_pais']
    list_filter = ['estatus_pais']  
##################### Admin de estados  ################# 
@admin.register(SeCatEstado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('rowid_edo','rowid_pais','id_edo','descri_largo_edo','descri_corto_edo','estatus_edo')
    search_fields = ['rowid_edo', 'descri_largo_edo']
    list_filter = ['estatus_edo']
##################### Admin de Municipios/Delegaciones  ############### 
@admin.register(SeCatMunicipioDelegacion)
class MunicipioDelegacionAdmin(admin.ModelAdmin):
    list_display = ('rowid_mundel','rowid_edo','id_mundel','descri_largo_mundel','descri_corto_mundel','estatus_mundel')
    search_fields = ['id_mundel', 'descri_largo_mundel']
    list_filter = ['estatus_mundel']
##################### Asentamiento ################################
class AsentamientoResources(resources.ModelResource):
    fields = ('rowid_asentamiento', 'id_asentamiento', 'descri_largo_asentamiento', 'descri_corto_asentamiento', 'estatus_asentamiento')
    class Meta:
        model = SeCatAsentamiento
@admin.register(SeCatAsentamiento)
class AsentamientoAdmin(ImportExportModelAdmin):
    resources_class = AsentamientoResources
    list_display = ('rowid_asentamiento', 'id_asentamiento', 'descri_largo_asentamiento', 'descri_corto_asentamiento', 'estatus_asentamiento')
    search_fields = ['rowid_asentamiento', 'descri_largo_asentamiento', 'descri_corto_asentamiento']
    list_filter = ['estatus_asentamiento']
# ##################### Admin de Colonias  ###################### 
@admin.register(SeCatColonia)
class ColoniaAdmin(admin.ModelAdmin):
    list_display = ('rowid_col','rowid_mundel','id_col','descri_largo_col','descrip_corto_col','estatus_col','codposcol')
    search_fields = ['id_col', 'descri_largo_col']
    list_filter = ['estatus_col']

# -------------------------------------------- Universidad --------------------------------------------- #

##################### Admin Universidad #################
@admin.register(SeCatUniversidad)
class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('rowid_uni', 'rowid_col', 'id_uni', 'nombre_uni', 'tipo_org_uni', 'direccion_uni', 'rfc_uni',
                        'codpos_uni', 'telefono1_uni', 'telefono2_uni', 'telefono3_uni', 'ext1_uni',
                        'ext2_uni', 'ext3_uni', 'mail_uni', 'pagina_internet_uni', 'contacto_uni', 'estatus_uni')
    search_fields = ['rowid_uni', 'id_uni']
    list_filter = ['estatus_uni']
##################### Admin Universidad #################
@admin.register(SeCatDivision)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('rowid_uni','rowid_div','id_div','descri_larga_div','descri_corta_div',
                    'representante_div','telefono_1_div','telefono_2_div','extension1_div','extension2_div','mail_div','estatus_div')
    search_fields = ['rowid_div', 'descri_larga_div']
    list_filter = ['estatus_div']
#################### Admin Carreras ##########################
@admin.register(SeCatCarrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('rowid_car', 'rowid_div', 'id_car', 'descri_largo_car','descri_corto_car',
                    'estatus_car','ceneval_car','descri_largo_tit')
    search_fields = ['id_car', 'descri_largo_car']
    list_filter = ['estatus_car']
#################### Admin Periodos ##########################
@admin.register(SeCatPeriodos)
class PeriodosAdmin(admin.ModelAdmin):
    list_display = ('rowid_per', 'rowid_car', 'evento_per', 'consecutivo_per','fecha_inicial_per',
                    'fecha_final_per','anio_per','periodo_per','descripcion_per','estatus_per')
    search_fields = ['evento_per', 'consecutivo_per']
    list_filter = ['estatus_per']

# -------------------------------------------- Plan de Estudios --------------------------------------------- #

##################### Admin de Plan de estudio  ################# 
@admin.register(SeCatPlaEstudio)
class PlanEstudioAdmin(admin.ModelAdmin):
    list_display = ('id_plan_est','decri_larga_plan_est','descri_corta_plan_est','estatus_plan_est','fec_alta_estpla','user_alta_estpla','fec_baja_estpla','user_baja_estpla')
    search_fields = ['id_plan_est']
    list_filter = ['estatus_plan_est'] 
##################### Admin Asignatura  ################# 
@admin.register(SeCatAsignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display =('rowid_asignatura', 'rowid_plan_est' , 'rowid_car' ,'id_asignatura', 'descri_larga_asi' ,'descri_corto_asi' ,'estatus_asi')
    search_fields = ['rowid_asignatura']
    list_filter = ['estatus_asi']
##################### Admin de Indicadores  ################# 
@admin.register(SeCatIndicador)
class IndicadoresAdmin(admin.ModelAdmin):
    list_display = ('id_indicador','descri_largo_ind','descri_corto_ind','estatus_ind','cve_control_ind')
    search_fields = ['id_indicador']
    list_filter = ['estatus_ind'] 
################plan de estudios asignatira admin
@admin.register(SeProPlanEstudio)
class PeaAdmin(admin.ModelAdmin):
    list_display = ('rowid_pro_plan_est','rowid_asignatura','rowid_plan_est','rowid_grado','rowid_car', 'horas_plan_est','creditos_plan_est', 'nota_minima_apro_est', 'valor_pon_final', 'estatus_pea')
    search_fields = ['rowid_pro_plan_est']
    list_filter = ['estatus_pea']
################ admin de plan de estudio asignatura
@admin.register(SeProAsiIndicador)
class PeaiAdmin(admin.ModelAdmin):
    list_display = ('rowid_pro_asi_ind' ,'rowid_pro_plan_est', 'rowid_indicador', 'porcentaje_pro_asi_idi' ,'comen_pro_asi_ind', 'estatus_peai')
    search_fields = ['rowid_pro_asi_ind']
    list_filter = ['estatus_peai']
 
# -------------------------------------------- Aspirantes --------------------------------------------- #

##################### Escuela de Procedencia ################################
class EscProcResources(resources.ModelResource):
    fields = ('rowid_esc_proc', 'rowid_mundel', 'cct_esc_proc', 'nombre_esc_proc', 'control_esc_proc', 'servicio_esc_proc', 'estatus_esc_proc')
    class Meta:
        model = SeCatEscuelaProcedencia
@admin.register(SeCatEscuelaProcedencia)
class EscProcAdmin(ImportExportModelAdmin):
    resources_class = EscProcResources
    list_display = ('rowid_esc_proc', 'rowid_mundel', 'cct_esc_proc', 'nombre_esc_proc', 'control_esc_proc', 'servicio_esc_proc', 'estatus_esc_proc')
    search_fields = ['rowid_esc_proc', 'cct_esc_proc', 'nombre_esc_proc', 'estatus_esc_proc']
    list_filter = ['estatus_esc_proc']
##################### Admin de Medio de difusion ################# 
@admin.register(SeCatMedioDifusion)
class MedioDifusionAdmin(admin.ModelAdmin):
    list_display = ('rowid_medio_dif','id_medio_dif','descri_largo_meddif','descri_corto_meddif','estatus_dif')
    search_fields = ['id_medio_dif', 'descri_largo_meddif']
    list_filter = ['estatus_dif']
##################### Admin de Tipos de escuelas ################# 
@admin.register(SeCatTipoEscuela)
class TipoEscuelaAdmin(admin.ModelAdmin):
    list_display = ('rowid_tipo_esc','rowid_col','id_tipo_esc','descri_largo_esc','descri_corta_esc','institucion','nombre_plantel','estatus_esc')
    search_fields = ['rowid_tipo_esc', 'descri_largo_esc']
    list_filter = ['estatus_esc']
##################### Admin de área bachillerato ################# 
@admin.register(SeCatAreaBachillerato)
class AreaBachiAdmin(admin.ModelAdmin):
    list_display = ('rowid_area_bac','id_area_bac','descri_larga_bac','descri_corta_bac','estatus_bac')
    search_fields = ['rowid_area_bac', 'descri_larga_bac']
    list_filter = ['estatus_bac']
##################### Admin de Indicador-Aspirante ############
@admin.register(SeProIndAsp)
class IndAspAdmin(admin.ModelAdmin):
    list_display = ('rowid_pro_ind_asp','rowid_car','rowid_indicador','valor_porcentual','estatus_indicadores')
    search_fields = ['rowid_pro_ind_asp', 'valor_porcentual']
    list_filter = ['estatus_indicadores']

# -------------------------------------------------------- APARTADO ESTUDIANTES -------------------------------------------------- #


##################### Admin de Plan de estudio  ################# 
@admin.register(SeTabEstudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('rowid_matricula', 'rowid_becas', 'rowid_car', 'rowid_col','rowid_mundel','rowid_esc_proc', 'rowid_grupo', 'id_matricula', 'nombre_estu',
    'paterno_est', 'materno_est', 'rfc_est', 'curp_est', 'direccion_est', 'telefono_est', 'email_est', 'sexo_est', 'fecha_alta_est', 'user_alta_est',
    'fecha_cambio_est', 'user_cambio_est', 'estatus_est', 'codpos', 'fec_nac_est', 'turno_est', 'generacion_est', 'periodo_est', 'anio_est',
    'estado_civil_est', 'mat_tutor_est', 'pat_tutor_est', 'nombre_tutor_est', 'no_folio_est',  'trabaja_est', 'tipo_sangre_est',
    'id_tipo_esc_est', 'id_area_bach_est', 'fecha_ini_bach', 'fecha_fin_bach', 'promedio_gral_bach', 'tel_trabajo',
    'edad_est', 'fecha_vig_est', 'estatus_inscri_est', 'imss_est', 'clinica_est', 'num_servicio', 'fec_ser_social', 'fecha_repos_est',
    'matri_est', 'beca_pro_est', 'usuario_est', 'password_est', 'estatus_biblio', 'tipo_carrera_est', 'otras_uts', 'otras_uts',
    'no_cedula_tsu', 'no_referencia', 'grasc', 'institucion_seguro', 'otrainstitucionseguro', 'nacionalidad',
    'discapacidad', 'tipodiscapacidad', 'foliocertificado', 'fechaexpedicioncer', 'equivalencia', 'parentescotutor', 'tipoestudiante',
    'num_ext', 'num_int')
    search_fields =['rowid_matricula']
    list_filter = ['estatus_est']
###############  Documentación  ##################
@admin.register(SeCatDocumentacion)
class DocumentacionAdmin(admin.ModelAdmin):
    list_display = ('rowid_doc', 'id_doc' ,'descri_corto_doc' ,'descri_largo_doc' ,'importante_doc', 'cve_control_doc' ,'estatus_grado', 'estatus_doc' )
    search_fields =['rowid_doc']
    list_filter = ['estatus_doc']
##################### Grupo ######################
@admin.register(SeCatGrupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('rowid_grupo','rowid_car','rowid_grado','id_grupo','descri_largo_gpo','descri_corto_gpo','lim_gpo','lim_acu_gpo','lim_rec_gpo','lim_acu_rec_gpo','estatus_gpo')
    search_fields =['rowid_grupo']
    list_filter = ['estatus_gpo']
############### Estatus Estudiante ###############
@admin.register(SeCatEstatusEstudiante)
class EstatusEstAdmin(admin.ModelAdmin):
    list_display = ('rowid_evento_est', 'id_evento_est' ,'consecutivo_est' ,'descri_largo_tipo_est', 'descri_largo_tipo_est', 'estatus_tipo_est')
    search_fields =['rowid_evento_est']
    list_filter = ['estatus_tipo_est']
# ##################### Admin de Grado  ####################### 
@admin.register(SeCatSalones)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('rowid_salon','rowid_car','id_salon','descri_corto_salon','descri_largo_salon','estatus_salon','tipo_salon','compartido_salon')
    search_fields = ['rowid_salon','descri_largo_salon','descri_corto_salon']
    list_filter = ['estatus_salon'] 
# ##################### Admin de Grado  ####################### 
@admin.register(SeCatGrado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('rowid_grado','id_grado','descri_corto_gra','estatus_gra')
    search_fields = ['rowid_grado','descri_corto_gra']
    list_filter = ['estatus_gra'] 
##################### Admin de becas ########################## 
@admin.register(SeCatBecas)
class BecasAdmin(admin.ModelAdmin):
    list_display = ('rowid_becas','id_becas','valor_ini_bec','valor_fin_bec','porcentaje_beca','estatus_bec')
    search_fields = ['rowid_becas', 'valor_ini_bec','valor_fin_bec']
    list_filter = ['estatus_bec']
##################### Admin de Tipo Cambio #################### 
@admin.register(SeCatTipoCambio)
class CambioAdmin(admin.ModelAdmin):
    list_display = ('rowid_tipo_cambio','id_tipo_cambio','descri_tipocambio','status')
    search_fields = ['rowid_tipo_cambio', 'id_tipo_cambio','descri_tipocambio']
    list_filter = ['status']
##################### Admin de Tipo Bajas ##################### 
@admin.register(SeCatTipoBajas)
class BajasAdmin(admin.ModelAdmin):
    list_display = ('rowid_tipo_baj','id_tipo_baj','descri_largo_tipo_baj','descri_corto_tipo_baj','estatus_tipo_baj')
    search_fields = ['rowid_tipo_baj', 'descri_largo_tipo_baj']
    list_filter = ['estatus_tipo_baj']

# -------------------------------------------- Empleados --------------------------------------------- #

##################### Empleado  ################# 
@admin.register(SeCatEmpleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('rowid_empleado','rowid_academico', 'rowid_car', 'rowid_depto','rowid_edo' ,'rowid_col', 'rowid_sueldo', 'id_empleado',
                    'nombre_emp', 'paterno_emp', 'materno_emp', 'rfc_emp', 'curp_emp', 'direccion_emp', 'telefono_emp', 'email_emp', 'sexo_emp',
                    'fecha_alta_emp', 'user_alta_emp', 'user_cambio_emp', 'fecha_cambio_emp', 'estatus_emp', 'codpos_emp', 'horas_contra_emp',
                    'fec_nac_emp', 'estatus_val', 'estatus_comp', 'edad_emp', 'estado_civil_emp', 'num_vac_max', 'num_vac_act', 'tipo_contrato_com',
                    'cedula_emp_com', 'fecicon', 'fecfcon', 'comentario_emp', 'estatus_biblio')
    search_fields = ['rowid_empleado', 'nombre_emp']
    list_filter = ['estatus_emp']
##################### Admin de Nivel Academco  ################# 
@admin.register(SeCatNivelAcademico)
class NivelAcademicoAdmin(admin.ModelAdmin):
    list_display = ('rowid_academico','id_academico','descri_largo_acade','descri_corto_acade','estatus_acade')
    search_fields = ['id_academico','descri_largo_acade']
    list_filter = ['estatus_acade']
##################### Admin de Plaza  ################# 
@admin.register(SeCatPlaza)
class PlazaAdmin(admin.ModelAdmin):
    list_display = ('rowid_plaza','id_plaza','descri_largo_plaza','descri_corto_plaza','estatus_plaza')
    search_fields = ['id_plaza','descri_largo_plaza']
    list_filter = ['estatus_plaza']
########################## Tipo Puesto ##########################
@admin.register(SeCatTipoPuesto)
class TipoPueAdmin(admin.ModelAdmin):
    list_display = ('rowid_puesto','rowid_plaza','id_puesto','descri_largo_pue','descri_corto_pue','estatus_pue')
    search_fields = ['id_puesto','descri_largo_pue']
    list_filter = ['estatus_pue']
########################## Sueldo ##########################
@admin.register(SeCatSueldos)
class SueldoAdmin(admin.ModelAdmin):
    list_display = ('rowid_puesto','rowid_sueldo','id_sueldo','sueldo','estatus_sueldo')
    search_fields = ['sueldo']
    list_filter = ['estatus_sueldo']
##################### Adscripciones  ################# 
@admin.register(SeCatDeptoEmp)
class AdscripcionesAdmin(admin.ModelAdmin):
    list_display = ('rowid_depto','id_depto','conse_depto','descri_largo_dep_emp','descri_corto_dep_emp','titular_depto','clave_ser','estatus_depto')
    search_fields = ['descri_largo_dep_emp']
    list_filter = ['estatus_depto'] 
##################### Actividades  ################# 
@admin.register(SeCatActividades)
class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('rowid_actividad','id_actividad','descri_largo_act','descri_corto_act','estatus_act')
    search_fields = ['descri_largo_act']
    list_filter = ['estatus_act'] 
##################### Instituciones  ################# 
@admin.register(SeCatInstitucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('rowid_institucion','id_institucion','descri_largo_ins','descri_corto_ins','estatus_ins')
    search_fields = ['descri_largo_ins']
    list_filter = ['estatus_ins'] 
##################### SeTabEmpCar  ################# 
@admin.register(SeTabEmpCar)
class EmpCarnAdmin(admin.ModelAdmin):
    list_display = ('rowid_emp_car','rowid_empleado','rowid_institucion','descri_corto_car_emp','descri_largo_car_emp',  'estatus_inst')
    search_fields = ['descri_corto_car_emp']
    list_filter = ['estatus_inst'] 

# -------------------------------------------- Operaciones  --------------------------------------------- #

#####################  Captura aspirante  ################# 
@admin.register(SeTabAspirante)
class AspiranteAdmin(admin.ModelAdmin):
    list_display = ('rowid_asp', 'rowid_mundel',  'rowid_area_bac', 'rowid_medio_dif', 'rowid_esc_proc', 'rowid_car' , 'rowid_tipo_esc','rowid_col', 
    'folio_utn_asp', 'fecha_alt_asp', 'calle_asp', 'num_int_asp' , 'num_ext_asp', 'codigo_postal_asp', 'tel_cas_asp', 'telefono_oficina_asp', 'sexo_asp', 'edad_asp',
    'estado_civil_asp', 'trabaja_asp', 'tipo_de_sangre_asp', 'promedio_asp' , 'fecini_bach_asp', 'fecfin_bach_asp', 'rfc_asp', 'curp_asp', 'fecha_nac_asp', 'materno_asp', 
    'paterno_asp', 'folio_cen_asp', 'nombre_asp', 'periodo_asp', 'anio_asp', 'mat_tutor_asp', 'pat_tutor_asp', 'nombre_tutor_asp', 'generacion_asp', 'turno_asp', 'user_alta', 'user_cambio',
    'email_asp' , 'opcioneducativa', 'continuidadestudio', 'otromediodif', 'otromedioinf', 'otroopcioneduca', 'facebook', 'twitter', 'discapacidad', 'tipodiscapacidad',
    'serviciomedico' ,'institucionseguro', 'otrainstitucionseguro' ,'numafiliacion', 'fechaexpedicioncer', 'folio', 'fechacompromisocerti', 'indigena', 'poblacionindigena', 'lenguaindigena','estatus_asp')
    search_fields = ['folio_utn_asp', 'paterno_asp']
    list_filter = ['estatus_asp']
##################### Captura aspirante ################# 
@admin.register(SeProAspDocu)
class DocuAdmin(admin.ModelAdmin):
    list_display = ('rowid_asp_docu','rowid_asp', 'rowid_doc','import_doc','entrego_doc',
    'comentario_doc', 'fecha_alta_doc', 'user_alta_doc', 'fecha_baja_doc', 'user_baja_doc', 'fecha_cambio_doc', 'user_cambio_doc', 'estatus_doc_aspi')
    search_fields = ['rowid_asp_docu']
    list_filter = ['estatus_doc_aspi']
#################### calificaciones aspi
@admin.register(SeTabAceptados)
class AceptadosAdmin(admin.ModelAdmin):
    list_display = ('rowid_ace','rowid_asp', 'rowid_indicador', 'calificacion_ace', 'folio_cen_ace','estatus_ace')
    search_fields = ['rowid_ace']
    list_filter = ['estatus_ace']
