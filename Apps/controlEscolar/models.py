from django.db import models

# Create your models here.
# -------------------------------------------- Direcciones --------------------------------------------- #

############################################## Tabla paises ############################################
class SeCatPais(models.Model):
    rowid_pais = models.AutoField(primary_key=True)
    id_pais = models.IntegerField(blank=True, null=True)
    descri_largo_pais = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_pais = models.CharField(max_length=10, blank=True, null=True)
    estatus_pais = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_pais'

    def __str__(self):
        texto="{0} / {1} / {2} "
        return texto.format(self.id_pais, self.descri_largo_pais, self.descri_corto_pais)
############################################## Tabla Estados ############################################
class SeCatEstado(models.Model):
    rowid_edo = models.AutoField(primary_key=True)
    rowid_pais = models.ForeignKey('SeCatPais', models.DO_NOTHING, db_column='rowid_pais', blank=True, null=True)
    id_edo = models.IntegerField(blank=True, null=True)
    descri_largo_edo = models.CharField(max_length=50)
    descri_corto_edo = models.CharField(max_length=10)
    estatus_edo = models.CharField(max_length=1, blank=True, null=True, default="A")
    class Meta:
        managed = False
        db_table = 'se_cat_estado'

    def __str__(self):
        texto="{0} / {1} / {2}"
        return texto.format(self.id_edo, self.descri_largo_edo, self.descri_corto_edo)
############################################## Tabla Municipio Delegacion ############################################
class SeCatMunicipioDelegacion(models.Model):
    rowid_mundel = models.AutoField(primary_key=True)
    rowid_edo = models.ForeignKey(SeCatEstado, models.DO_NOTHING, db_column='rowid_edo', blank=True, null=True)
    id_mundel = models.IntegerField()
    descri_largo_mundel = models.CharField(max_length=50)
    descri_corto_mundel = models.CharField(max_length=10)
    estatus_mundel = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_municipio_delegacion'
    
    def __str__(self):
        texto="{0} - {1} "
        return texto.format(self.id_mundel, self.descri_largo_mundel)
############################################## Tabla Colonias ############################################
class SeCatColonia(models.Model):
    rowid_col = models.AutoField(primary_key=True)
    rowid_mundel = models.ForeignKey('SeCatMunicipioDelegacion', models.DO_NOTHING, db_column='rowid_mundel', blank=True, null=True)
    id_col = models.IntegerField()
    descri_largo_col = models.CharField(max_length=50)
    descrip_corto_col = models.CharField(max_length=10)
    codposcol = models.CharField(max_length=5, blank=True, null=True)
    estatus_col = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_colonia'

    def __str__(self):
        texto="{0}-{1}"
        return texto.format(self.id_col, self.descri_largo_col)

# -------------------------------------------- Universidad --------------------------------------------- #

############################################## Tabla Universidades ############################################
class SeCatUniversidad(models.Model):
    rowid_uni = models.IntegerField(primary_key=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    id_uni = models.IntegerField()
    nombre_uni = models.CharField(max_length=60)
    tipo_org_uni = models.CharField(max_length=100, blank=True, null=True)
    direccion_uni = models.CharField(max_length=60)
    rfc_uni = models.CharField(max_length=15)
    codpos_uni = models.CharField(max_length=5)
    telefono1_uni = models.CharField(max_length=15)
    telefono2_uni = models.CharField(max_length=15, blank=True, null=True)
    telefono3_uni = models.CharField(max_length=15, blank=True, null=True)
    ext1_uni = models.CharField(max_length=7, blank=True, null=True)
    ext2_uni = models.CharField(max_length=7, blank=True, null=True)
    ext3_uni = models.CharField(max_length=7, blank=True, null=True)
    mail_uni = models.CharField(max_length=30, blank=True, null=True)
    pagina_internet_uni = models.CharField(max_length=35, blank=True, null=True)
    contacto_uni = models.CharField(max_length=50)
    estatus_uni = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_universidad'

    def __str__(self):
        texto = "{0}-{1} "
        return texto.format(self.rowid_uni, self.nombre_uni)
############################################## Tabla Divisiones ############################################
class SeCatDivision(models.Model):
    rowid_div = models.IntegerField(primary_key=True)
    rowid_uni = models.ForeignKey(SeCatUniversidad, models.DO_NOTHING, db_column='rowid_uni', blank=True, null=True)
    id_div = models.IntegerField()
    descri_larga_div = models.CharField(max_length=50)
    descri_corta_div = models.CharField(max_length=10)
    representante_div = models.CharField(max_length=50)
    telefono_1_div = models.CharField(max_length=15, blank=True, null=True)
    telefono_2_div = models.CharField(max_length=15, blank=True, null=True)
    extension1_div = models.CharField(max_length=7, blank=True, null=True)
    extension2_div = models.CharField(max_length=7, blank=True, null=True)
    mail_div = models.CharField(max_length=25, blank=True, null=True)
    estatus_div = models.CharField(max_length=1, blank=True, null=True, default="A")
    class Meta:
        managed = False
        db_table = 'se_cat_division'
    def __str__(self):
        texto="{0} / {1} "
        return texto.format(self.descri_larga_div, self.descri_corta_div)
############################ Carreras ##########################################
class SeCatCarrera(models.Model):
    rowid_car = models.AutoField(primary_key=True)
    rowid_div = models.ForeignKey('SeCatDivision', models.DO_NOTHING, db_column='rowid_div', blank=True, null=True)
    id_car = models.IntegerField()
    descri_largo_car = models.CharField(max_length=50)
    descri_corto_car = models.CharField(max_length=10)
    estatus_car = models.CharField(max_length=1, blank=True, null=True, default="A")
    ceneval_car = models.CharField(max_length=1, blank=True, null=True)
    descri_largo_tit = models.CharField(max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_carrera'
    
    def __str__(self):
        texto="{0}-{1} "
        return texto.format(self.rowid_car, self.descri_largo_car)
################################ Periodos ######################################
class SeCatPeriodos(models.Model):
    rowid_per = models.AutoField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    evento_per = models.CharField(max_length=3)
    consecutivo_per = models.IntegerField()
    fecha_inicial_per = models.DateField(blank=True, null=True)
    fecha_final_per = models.DateField(blank=True, null=True)
    anio_per = models.IntegerField(blank=True, null=True)
    periodo_per = models.IntegerField(blank=True, null=True)
    descripcion_per = models.CharField(max_length=255, blank=True, null=True)
    estatus_per = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_periodos'
    
    def __str__(self):
        texto="{0}-{1} "
        return texto.format(self.rowid_per, self.evento_per)

# -------------------------------------------- Aspirantes --------------------------------------------- #

############################################## Tabla Medios de Difusión ################################
class SeCatMedioDifusion(models.Model):
    rowid_medio_dif = models.IntegerField(primary_key=True)
    id_medio_dif = models.IntegerField()
    descri_largo_meddif = models.CharField(max_length=50)
    descri_corto_meddif = models.CharField(max_length=10)
    estatus_dif = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_medio_difusion'

    def __str__(self):
        texto="{0} / {1} "
        return texto.format(self.descri_largo_meddif, self.descri_corto_meddif)
############################################## Tabla Tipos de escuelas   ###############################
class SeCatTipoEscuela(models.Model):
    rowid_tipo_esc = models.IntegerField(primary_key=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    id_tipo_esc = models.IntegerField()
    descri_largo_esc = models.CharField(max_length=50)
    descri_corta_esc = models.CharField(max_length=10)
    estatus_esc = models.CharField(max_length=1, blank=True, null=True, default="A")
    institucion = models.CharField(max_length=50, blank=True, null=True)
    nombre_plantel = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_tipo_escuela'

    def __str__(self):
        texto="{0} / {1} "
        return texto.format(self.descri_largo_esc, self.descri_corta_esc)
############################################## Tabla Areas de Bachillerato #############################
class SeCatAreaBachillerato(models.Model):
    rowid_area_bac = models.IntegerField(primary_key=True)
    id_area_bac = models.IntegerField()
    descri_larga_bac = models.CharField(max_length=50)
    descri_corta_bac = models.CharField(max_length=10)
    estatus_bac = models.CharField(max_length=1, blank=True, null=True , default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_area_bachillerato'

    def __str__(self):
        texto="{0} / {1}"
        return texto.format(self.descri_larga_bac, self.descri_corta_bac)
############################################## APARTADO indicador se ocupa##########################################################
class SeCatIndicador(models.Model):
    id_indicador = models.IntegerField(primary_key=True)
    descri_largo_ind = models.CharField(max_length=50)
    descri_corto_ind = models.CharField(max_length=10)
    estatus_ind = models.CharField(max_length=1, blank=True, null=True, default="A")
    cve_control_ind = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'se_cat_indicador'

    def __str__(self):
        texto="{0} / {1}"
        return texto.format(self.descri_largo_ind, self.descri_corto_ind)
############################################## Tabla Indicadores Aspirantes ############################
class SeProIndAsp(models.Model):
    rowid_pro_ind_asp = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_indicador = models.ForeignKey(SeCatIndicador, models.DO_NOTHING, db_column='rowid_indicador', blank=True, null=True)
    valor_porcentual = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    estatus_indicadores = models.CharField(max_length=1, blank=True, null=True, default="A")
    class Meta:
        managed = False
        db_table = 'se_pro_ind_asp'
    def __str__(self):
        texto = "{0} / {1}"
        return texto.format(self.rowid_pro_ind_asp, self.valor_porcentual)

# -------------------------------------------- Estudiantes --------------------------------------------- #

# ############################################## APARTADO SALONES ######################################
class SeCatSalones(models.Model):
    rowid_salon = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    id_salon = models.IntegerField()
    descri_corto_salon = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_salon = models.CharField(max_length=50, blank=True, null=True)
    estatus_salon = models.CharField(max_length=1, blank=True, null=True, default="A")
    tipo_salon = models.CharField(max_length=3, blank=True, null=True)
    compartido_salon = models.CharField(max_length=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'se_cat_salones'
    def __str__(self):
        texto="{0} / {1}"
        return texto.format(self.descri_largo_salon, self.descri_corto_salon)
# ############################################## APARTADO GRADOS #######################################
class SeCatGrado(models.Model):
    rowid_grado = models.IntegerField(primary_key=True)
    id_grado = models.IntegerField()
    descri_corto_gra = models.CharField(max_length=10)
    estatus_gra = models.CharField(max_length=1, blank=True, null=True, default="A")
    class Meta:
        managed = False
        db_table = 'se_cat_grado'
    def __str__(self):
        texto="{0} / {1}"
        return texto.format(self.id_grado, self.descri_corto_gra) 
##############################################  Tabla Becas   ##########################################
class SeCatBecas(models.Model):
    rowid_becas = models.IntegerField(primary_key=True)
    id_becas = models.IntegerField()
    valor_ini_bec = models.DecimalField(max_digits=6, decimal_places=2)
    valor_fin_bec = models.DecimalField(max_digits=6, decimal_places=2)
    porcentaje_beca = models.DecimalField(max_digits=6, decimal_places=2)
    estatus_bec = models.CharField(max_length=1, blank=True, null=True, default="A")
    class Meta:
        managed = False
        db_table = 'se_cat_becas'
    def __str__(self):
        texto="{0} / {1} / {2} / {3} / {4}"
        return texto.format(self.id_becas, self.valor_ini_bec, self.valor_fin_bec, self.porcentaje_beca, self.estatus_bec)
############################################## Tabla Tipo Cambio #######################################
class SeCatTipoCambio(models.Model):
    rowid_tipo_cambio = models.IntegerField(primary_key=True)
    id_tipo_cambio = models.IntegerField()
    descri_tipocambio = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True, default="A")
    class Meta:
        managed = False
        db_table = 'se_cat_tipo_cambio'
    def __str__(self):
        texto="{0} / {1} / {2} "
        return texto.format(self.id_tipo_cambio, self.descri_tipocambio, self.status)
############################################## Tabla Tipos de Baja #####################################
class SeCatTipoBajas(models.Model):
    rowid_tipo_baj = models.IntegerField(primary_key=True)
    id_tipo_baj = models.IntegerField()
    descri_largo_tipo_baj = models.CharField(max_length=50)
    descri_corto_tipo_baj = models.CharField(max_length=10)
    estatus_tipo_baj = models.CharField(max_length=1, blank=True, null=True, default="A")
    class Meta:
        managed = False
        db_table = 'se_cat_tipo_bajas'
    def __str__(self):
        texto="{0} / {1}"
        return texto.format(self.descri_largo_tipo_baj, self.descri_corto_tipo_baj)


# -------------------------------------------- Empleados --------------------------------------------- #

############################################## Tabla Adscripciones ############################################
class SeCatDeptoEmp(models.Model):
    rowid_depto = models.AutoField(primary_key=True)
    id_depto = models.CharField(max_length=3)
    conse_depto = models.IntegerField()
    descri_largo_dep_emp = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_dep_emp = models.CharField(max_length=10, blank=True, null=True)
    titular_depto = models.CharField(max_length=60, blank=True, null=True)
    clave_ser = models.IntegerField(blank=True, null=True)
    estatus_depto = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_depto_emp'
    def __str__(self):
        texto="{0}-{1}"
        return texto.format(self.id_depto, self.descri_largo_dep_emp)
############################# EMPLEADO #########################################
class SeCatEmpleado(models.Model):
    rowid_empleado = models.IntegerField(primary_key=True)
    rowid_academico = models.ForeignKey('SeCatNivelAcademico', models.DO_NOTHING, db_column='rowid_academico', blank=True, null=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_depto = models.ForeignKey(SeCatDeptoEmp, models.DO_NOTHING, db_column='rowid_depto', blank=True, null=True)
    rowid_edo = models.ForeignKey('SeCatEstado', models.DO_NOTHING, db_column='rowid_edo', blank=True, null=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    rowid_sueldo = models.ForeignKey('SeCatSueldos', models.DO_NOTHING, db_column='rowid_sueldo', blank=True, null=True)
    id_empleado = models.IntegerField()
    nombre_emp = models.CharField(max_length=40)
    paterno_emp = models.CharField(max_length=30)
    materno_emp = models.CharField(max_length=30)
    rfc_emp = models.CharField(max_length=15)
    curp_emp = models.CharField(max_length=25)
    direccion_emp = models.CharField(max_length=60)
    telefono_emp = models.CharField(max_length=15, blank=True, null=True)
    email_emp = models.CharField(max_length=35, blank=True, null=True)
    sexo_emp = models.CharField(max_length=1)
    fecha_alta_emp = models.DateField(blank=True, null=True)
    user_alta_emp = models.CharField(max_length=10, blank=True, null=True)
    user_cambio_emp = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_emp = models.DateField(blank=True, null=True)
    estatus_emp = models.CharField(max_length=1, blank=True, null=True, default="A")
    codpos_emp = models.IntegerField()
    horas_contra_emp = models.IntegerField()
    fec_nac_emp = models.DateField()
    estatus_val = models.CharField(max_length=1, blank=True, null=True)
    estatus_comp = models.CharField(max_length=1, blank=True, null=True)
    edad_emp = models.IntegerField(blank=True, null=True)
    estado_civil_emp = models.CharField(max_length=1, blank=True, null=True)
    num_vac_max = models.IntegerField(blank=True, null=True)
    num_vac_act = models.IntegerField(blank=True, null=True)
    tipo_contrato_com = models.IntegerField(blank=True, null=True)
    cedula_emp_com = models.CharField(max_length=20, blank=True, null=True)
    fecicon = models.DateField(blank=True, null=True)
    fecfcon = models.DateField(blank=True, null=True)
    comentario_emp = models.CharField(max_length=30, blank=True, null=True)
    estatus_biblio = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_empleado'

    def __str__(self):
        texto="{0}-{1} {2} {3}"
        return texto.format(self.rowid_empleado, self.nombre_emp, self.paterno_emp, self.materno_emp)
############################################## Tabla Nivel Academico ###################################
class SeCatNivelAcademico(models.Model):
    rowid_academico = models.AutoField(primary_key=True)
    id_academico = models.IntegerField()
    descri_largo_acade = models.CharField(max_length=50)
    descri_corto_acade = models.CharField(max_length=10)
    estatus_acade = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_nivel_academico'

    def __str__(self):
        texto = "{0} / {1} / {2} / {3}"
        return texto.format(self.id_academico, self.descri_largo_acade, self.descri_corto_acade, self.estatus_acade)
############################################## Tabla Plazas ###################################
class SeCatPlaza(models.Model):
    rowid_plaza = models.AutoField(primary_key=True)
    id_plaza = models.IntegerField()
    descri_largo_plaza = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_plaza = models.CharField(max_length=10, blank=True, null=True)
    estatus_plaza = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_plaza'

    def __str__(self):
        texto = "{0}-{1}"
        return texto.format(self.id_plaza, self.descri_largo_plaza)
############################### TIPO PUESTO #############################################
class SeCatTipoPuesto(models.Model):
    rowid_puesto = models.AutoField(primary_key=True)
    rowid_plaza = models.ForeignKey(SeCatPlaza, models.DO_NOTHING, db_column='rowid_plaza', blank=True, null=True)
    id_puesto = models.IntegerField()
    descri_largo_pue = models.CharField(max_length=50)
    descri_corto_pue = models.CharField(max_length=10)
    estatus_pue = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_tipo_puesto'
    
    def __str__(self):
        texto="{0}-{1}"
        return texto.format(self.id_puesto, self.descri_largo_pue)
######################## SUELDOS ###########################
class SeCatSueldos(models.Model):
    rowid_sueldo = models.AutoField(primary_key=True)
    rowid_puesto = models.ForeignKey('SeCatTipoPuesto', models.DO_NOTHING, db_column='rowid_puesto', blank=True, null=True)
    id_sueldo = models.IntegerField()
    sueldo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estatus_sueldo = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_sueldos'

    def __str__(self):
        texto="{0}"
        return texto.format(self.sueldo)
############################################## Tabla Actividades ############################################
class SeCatActividades(models.Model):
    rowid_actividad = models.AutoField(primary_key=True)
    id_actividad = models.IntegerField()
    descri_largo_act = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_act = models.CharField(max_length=10, blank=True, null=True)
    estatus_act = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_actividades'
    def __str__(self):
        texto="{0}-{1}"
        return texto.format(self.rowid_actividad, self.descri_largo_act)
############################################## Tabla Instituciones de Egreso ############################################
class SeCatInstitucion(models.Model):
    rowid_institucion = models.AutoField(primary_key=True)
    id_institucion = models.IntegerField()
    descri_largo_ins = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_ins = models.CharField(max_length=10, blank=True, null=True)
    estatus_ins = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_cat_institucion'
    def __str__(self):
        texto="{0}-{1}"
        return texto.format(self.id_institucion, self.descri_largo_ins)
############################################## Tabla Carrera empleado  EmpCar ############################################
class SeTabEmpCar(models.Model):
    rowid_emp_car = models.AutoField(primary_key=True)
    rowid_institucion = models.ForeignKey(SeCatInstitucion, models.DO_NOTHING, db_column='rowid_institucion', blank=True, null=True)
    rowid_empleado = models.ForeignKey(SeCatEmpleado, models.DO_NOTHING, db_column='rowid_empleado', blank=True, null=True)
    descri_largo_car_emp = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_car_emp = models.CharField(max_length=10, blank=True, null=True)
    estatus_inst = models.CharField(max_length=1, blank=True, null=True, default="A")

    class Meta:
        managed = False
        db_table = 'se_tab_emp_car'
        
    def __str__(self):
        texto="{0}-{1}"
        return texto.format(self.rowid_empleado, self.descri_largo_car_emp)





############################################## APARTADO PLANES DE ESTUDIO ###############################################
class SeCatPlaEstudio(models.Model):
    id_plan_est = models.IntegerField(primary_key=True)
    decri_larga_plan_est = models.CharField(max_length=50)
    descri_corta_plan_est = models.CharField(max_length=10)
    estatus_plan_est = models.CharField(max_length=1, blank=True, null=True, default="A")
    fec_alta_estpla = models.DateField(blank=True, null=True)
    user_alta_estpla = models.CharField(max_length=10, blank=True, null=True)
    fec_baja_estpla = models.DateField(blank=True, null=True)
    user_baja_estpla = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_pla_estudio'

    def __str__(self):
        texto="{0} / {1}"
        return texto.format(self.decri_larga_plan_est, self.descri_corta_plan_est)


##############   Operaciones #################

############################################## TABLA ASPIRANTES ##########################################################
class SeTabAspirante(models.Model):
    folio_utn_asp = models.CharField(primary_key=True, max_length=20)
    rowid_area_bac = models.ForeignKey(SeCatAreaBachillerato, models.DO_NOTHING, db_column='rowid_area_bac', blank=True, null=True)
    rowid_medio_dif = models.ForeignKey(SeCatMedioDifusion, models.DO_NOTHING, db_column='rowid_medio_dif', blank=True, null=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_tipo_esc = models.ForeignKey(SeCatTipoEscuela, models.DO_NOTHING, db_column='rowid_tipo_esc', blank=True, null=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    fecha_alt_asp = models.DateField()
    mpo_o_alcaldia_nac_asp = models.IntegerField()
    ent_fed_nac_asp = models.IntegerField()
    calle_asp = models.CharField(max_length=60)
    num_int_asp = models.CharField(max_length=30, blank=True, null=True)
    num_ext_asp = models.CharField(max_length=30, blank=True, null=True)
    codigo_postal_asp = models.CharField(max_length=5)
    tel_cas_asp = models.CharField(max_length=30, blank=True, null=True)
    telefono_oficina_asp = models.CharField(max_length=15, blank=True, null=True)
    sexo_asp = models.CharField(max_length=1)
    edad_asp = models.IntegerField(blank=True, null=True)
    estado_civil_asp = models.CharField(max_length=1, blank=True, null=True)
    trabaja_asp = models.CharField(max_length=1, blank=True, null=True)
    tipo_de_sangre_asp = models.CharField(max_length=10, blank=True, null=True)
    promedio_asp = models.DecimalField(max_digits=5, decimal_places=2)
    fecini_bach_asp = models.IntegerField()
    fecfin_bach_asp = models.IntegerField()
    rfc_asp = models.CharField(max_length=15)
    curp_asp = models.CharField(max_length=25)
    nom_esc_pro_asp = models.CharField(max_length=150, blank=True, null=True)
    estatus_asp = models.CharField(max_length=1, blank=True, null=True)
    fecha_nac_asp = models.DateField()
    materno_asp = models.CharField(max_length=30)
    paterno_asp = models.CharField(max_length=30)
    folio_cen_asp = models.CharField(max_length=15, blank=True, null=True)
    nombre_asp = models.CharField(max_length=40)
    tipo_publica_privada = models.CharField(max_length=1, blank=True, null=True)
    periodo_asp = models.IntegerField(blank=True, null=True)
    anio_asp = models.IntegerField(blank=True, null=True)
    mat_tutor_asp = models.CharField(max_length=30, blank=True, null=True)
    pat_tutor_asp = models.CharField(max_length=30, blank=True, null=True)
    nombre_tutor_asp = models.CharField(max_length=40, blank=True, null=True)
    generacion_asp = models.IntegerField(blank=True, null=True)
    entidad_estudio = models.IntegerField(blank=True, null=True)
    municipio_estudio = models.IntegerField(blank=True, null=True)
    ronda_asp = models.IntegerField(blank=True, null=True)
    turno_asp = models.CharField(max_length=1, blank=True, null=True)
    user_alta = models.CharField(max_length=70, blank=True, null=True)
    user_cambio = models.CharField(max_length=70, blank=True, null=True)
    email_asp = models.CharField(max_length=50, blank=True, null=True)
    opcioneducativa = models.CharField(max_length=10, blank=True, null=True)
    continuidadestudio = models.CharField(max_length=10, blank=True, null=True)
    otromediodif = models.CharField(max_length=100, blank=True, null=True)
    otromedioinf = models.CharField(max_length=100, blank=True, null=True)
    otroopcioneduca = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    discapacidad = models.CharField(max_length=4, blank=True, null=True)
    tipodiscapacidad = models.CharField(max_length=25, blank=True, null=True)
    serviciomedico = models.CharField(max_length=4, blank=True, null=True)
    institucionseguro = models.CharField(max_length=25, blank=True, null=True)
    otrainstitucionseguro = models.CharField(max_length=40, blank=True, null=True)
    numafiliacion = models.CharField(max_length=20, blank=True, null=True)
    fechaexpedicioncer = models.CharField(max_length=20, blank=True, null=True)
    folio = models.CharField(max_length=40, blank=True, null=True)
    fechacompromisocerti = models.CharField(max_length=20, blank=True, null=True)
    indigena = models.CharField(max_length=4, blank=True, null=True)
    poblacionindigena = models.CharField(max_length=25, blank=True, null=True)
    lenguaindigena = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_aspirante'


