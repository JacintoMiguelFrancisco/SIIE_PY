from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import (SeCatPais, SeCatEstado, SeCatMunicipioDelegacion, SeCatColonia, SeCatUniversidad, SeCatNivelAcademico, SeCatPlaza, SeCatAreaBachillerato, 
                    SeCatTipoBajas,  SeCatBecas, SeCatMedioDifusion,SeCatTipoEscuela,SeCatTipoCambio,SeTabEmpCar,SeCatEmpleado, SeCatDivision, SeProIndAsp,
                    SeCatIndicador, SeCatPlaEstudio, SeCatGrado, SeCatDeptoEmp, SeCatActividades, SeCatInstitucion, SeCatCarrera, SeCatPeriodos, SeCatSalones)

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

# -------------------------------------------- Aspirantes --------------------------------------------- #

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








##################### Admin de Nivel Academco  ################# 
@admin.register(SeCatNivelAcademico)
class NivelAcademicoAdmin(admin.ModelAdmin):
    list_display = ('id_academico','descri_largo_acade','descri_corto_acade','estatus_acade')
    search_fields = ['id_academico','descri_largo_acade']
    list_filter = ['estatus_acade']

##################### Admin de Plaza  ################# 
@admin.register(SeCatPlaza)
class PlazaAdmin(admin.ModelAdmin):
    list_display = ('id_plaza','descri_largo_plaza','descri_corto_plaza','estatus_plaza')
    search_fields = ['id_plaza','descri_largo_plaza']
    list_filter = ['estatus_plaza']

##################### Admin de Indicadores  ################# 
@admin.register(SeCatIndicador)
class IndicadoresAdmin(admin.ModelAdmin):
    list_display = ('id_indicador','descri_largo_ind','descri_corto_ind','estatus_ind','cve_control_ind')
    search_fields = ['id_indicador']
    list_filter = ['estatus_ind'] 

##################### Admin de Plan de estudio  ################# 
@admin.register(SeCatPlaEstudio)
class PlanEstudioAdmin(admin.ModelAdmin):
    list_display = ('id_plan_est','decri_larga_plan_est','descri_corta_plan_est','estatus_plan_est','fec_alta_estpla','user_alta_estpla','fec_baja_estpla','user_baja_estpla')
    search_fields = ['id_plan_est']
    list_filter = ['estatus_plan_est'] 


# -------------------------------------------- Empleados --------------------------------------------- #

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

##################### Empleado  ################# 
admin.site.register(SeCatEmpleado)