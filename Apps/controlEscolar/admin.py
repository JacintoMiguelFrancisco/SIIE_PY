from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import (SeCatPais, SeCatEstado, SeCatMunicipioDelegacion, SeCatColonia, SeCatUniversidad, SeCatNivelAcademico, SeCatPlaza, SeCatAreaBachillerato, 
                    SeCatTipoBajas,  SeCatBecas, SeCatMedioDifusion,SeCatTipoEscuela,SeCatTipoCambio,
                    SeCatIndicador, SeCatPlaEstudio, SeCatGrado, SeCatDeptoEmp, SeCatActividades, SeCatInstitucion)

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




##################### Admin Universidad ################# 
@admin.register(SeCatUniversidad)
class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('id_pais','id_edo','id_mundel','id_col', 'id_uni', 'nombre_uni', 'tipo_org_uni','direccion_uni', 'rfc_uni',
                    'codpos_uni','telefono1_uni','telefono2_uni','telefono3_uni','fax1_uni','fax2_uni','fax3_uni','ext1_uni',
                    'ext2_uni','ext3_uni','mail_uni','pagina_internet_uni','contacto_uni','estatus_uni')
    search_fields = ['id_uni', 'nombre_uni']
    list_filter = ['estatus_uni']

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

##################### Admin de Area Bachillerato  ################# 
@admin.register(SeCatAreaBachillerato)
class BachiAdmin(admin.ModelAdmin):
    list_display = ('id_area_bac', 'descri_larga_bac', 'descri_corta_bac', 'estatus_bac')
    search_fields = ['descri_larga_bac', 'descri_corta_bac']
    list_filter = ['estatus_bac']

##################### Admin de Tipo Bajas ################# 
@admin.register(SeCatTipoBajas)
class TipBajaAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_baj', 'descri_largo_tipo_baj', 'descri_corto_tipo_baj', 'estatus_tipo_baj')
    search_fields = ['descri_largo_tipo_baj', 'descri_corto_tipo_baj']
    list_filter = ['estatus_tipo_baj']

##################### Admin de Medio de difusion ################# 
@admin.register(SeCatMedioDifusion)
class MedioDifusionAdmin(admin.ModelAdmin):
    list_display = ('id_medio_dif','descri_largo_meddif','descri_corto_meddif','estatus_dif')
    search_fields = ['id_medio_dif', 'descri_largo_meddif']
    list_filter = ['estatus_dif']

##################### Admin de Tipo Escuela  ################# 
@admin.register(SeCatTipoEscuela)
class TipoEscuelaAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_esc','descri_largo_esc','descri_corta_esc','estatus_esc','id_edo','id_mundel','institucion','nombre_plantel')
    search_fields = ['id_tipo_esc', 'descri_largo_esc']
    list_filter = ['estatus_esc']

##################### Admin de Becas  ################# 
@admin.register(SeCatBecas)
class BecasAdmin(admin.ModelAdmin):
    list_display = ('id_becas','valor_ini_bec','valor_fin_bec','porcentaje_beca','estatus_bec')
    search_fields = ['id_becas']
    list_filter = ['estatus_bec']

##################### Admin de Tipo Cambio  ################# 
@admin.register(SeCatTipoCambio)
class TipoCambioAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_cambio','descri_tipocambio','status')
    search_fields = ['id_tipo_cambio']
    list_filter = ['status']

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

##################### Admin de Grado  ################# 
@admin.register(SeCatGrado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('id_grado','descri_corto_gra','estatus_gra')
    search_fields = ['id_grado']
    list_filter = ['estatus_gra'] 



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

##################### Actividades  ################# 
@admin.register(SeCatInstitucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('rowid_institucion','id_institucion','descri_largo_ins','descri_corto_ins','estatus_ins')
    search_fields = ['descri_largo_ins']
    list_filter = ['estatus_ins'] 
