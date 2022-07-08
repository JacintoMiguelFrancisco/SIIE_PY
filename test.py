# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    website = models.CharField(max_length=200)
    biography = models.TextField()
    phone_number = models.CharField(max_length=20)
    picture = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_profile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ControlescolarSecatpais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    descri_largo_pais = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_pais = models.CharField(max_length=10, blank=True, null=True)
    estatus_pais = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controlEscolar_secatpais'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Pagosalumnos(models.Model):
    fecha_deposito = models.DateField(blank=True, null=True)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    concepto = models.CharField(max_length=250, blank=True, null=True)
    importe = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    id_matricula = models.FloatField(primary_key=True)
    clave = models.IntegerField()
    estatus = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagosalumnos'
        unique_together = (('id_matricula', 'clave'), ('id_matricula', 'clave'),)


class Pagosalumnostitulacion(models.Model):
    fecha_deposito = models.DateField(blank=True, null=True)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    concepto = models.CharField(max_length=250, blank=True, null=True)
    importe = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    id_matricula = models.FloatField(primary_key=True)
    clave = models.IntegerField()
    estatus = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagosalumnostitulacion'
        unique_together = (('id_matricula', 'clave'), ('id_matricula', 'clave'),)


class Pagosrecuperacion(models.Model):
    folio = models.FloatField(primary_key=True)
    fecha = models.DateField()
    concepto = models.CharField(max_length=100, blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    parcial = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    id_matricula = models.FloatField(blank=True, null=True)
    usuarioalta = models.CharField(max_length=20, blank=True, null=True)
    fechaalta = models.DateField(blank=True, null=True)
    referencia = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pagosrecuperacion'


class SbCatAreasConocimiento(models.Model):
    rowid_area_cono = models.IntegerField(primary_key=True)
    id_area_cono = models.IntegerField()
    descri_larga_cono = models.CharField(max_length=50, blank=True, null=True)
    descri_corta_cono = models.CharField(max_length=10, blank=True, null=True)
    estatus_cono = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_cat_areas_conocimiento'


class SbCatEditorial(models.Model):
    rowid_editorial = models.IntegerField(primary_key=True)
    rowid_col = models.ForeignKey('SeCatColonia', models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    id_editorial = models.IntegerField()
    razon_social_edi = models.CharField(max_length=60, blank=True, null=True)
    direccion_edi = models.CharField(max_length=60, blank=True, null=True)
    contacto1_edi = models.CharField(max_length=50, blank=True, null=True)
    contacto2_edi = models.CharField(max_length=50, blank=True, null=True)
    rfc_edi = models.CharField(max_length=15, blank=True, null=True)
    codpos_edi = models.IntegerField(blank=True, null=True)
    telefono1_edi = models.CharField(max_length=15, blank=True, null=True)
    telefono2_edi = models.CharField(max_length=15, blank=True, null=True)
    telefono3_edi = models.CharField(max_length=15, blank=True, null=True)
    fax1_edi = models.CharField(max_length=15, blank=True, null=True)
    fax2_edi = models.CharField(max_length=15, blank=True, null=True)
    fax3_edi = models.CharField(max_length=15, blank=True, null=True)
    ext1_edi = models.CharField(max_length=7, blank=True, null=True)
    ext2_edi = models.CharField(max_length=7, blank=True, null=True)
    ext3_edi = models.CharField(max_length=7, blank=True, null=True)
    pagina_internet_edi = models.CharField(max_length=35, blank=True, null=True)
    mail_edi = models.CharField(max_length=30, blank=True, null=True)
    estatus_edi = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_cat_editorial'


class SbCatEstatusLibro(models.Model):
    rowid_edo_libro = models.IntegerField(primary_key=True)
    id_edo_libro = models.IntegerField()
    descri_corto_libro = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_libro = models.CharField(max_length=50, blank=True, null=True)
    estatus_cat_libro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_cat_estatus_libro'


class SbCatLibros(models.Model):
    rowid_ficha = models.IntegerField(primary_key=True)
    rowid_etiqueta = models.ForeignKey('SbTabEtiquetas', models.DO_NOTHING, db_column='rowid_etiqueta', blank=True, null=True)
    num_ficha = models.FloatField()
    descripcion_libro = models.CharField(max_length=255, blank=True, null=True)
    operador_marc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_cat_libros'


class SbContadorAsistencia(models.Model):
    id_uni = models.IntegerField(primary_key=True)
    id_div = models.IntegerField()
    id_car = models.IntegerField()
    fecha = models.DateField()
    asistencia = models.IntegerField(blank=True, null=True)
    visita = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_contador_asistencia'
        unique_together = (('id_uni', 'id_div', 'id_car', 'fecha'), ('id_uni', 'id_div', 'id_car', 'fecha'),)


class SbProEstatusLib(models.Model):
    rowid_edo_libro = models.OneToOneField(SbCatEstatusLibro, models.DO_NOTHING, db_column='rowid_edo_libro', primary_key=True)
    rowid_num_aquisicion = models.ForeignKey('SbTabAcervo', models.DO_NOTHING, db_column='rowid_num_aquisicion')
    feci_cat_libro = models.DateField(blank=True, null=True)
    fecf_cat_libro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_pro_estatus_lib'
        unique_together = (('rowid_edo_libro', 'rowid_num_aquisicion'), ('rowid_edo_libro', 'rowid_num_aquisicion'),)


class SbProMovEmpLibros(models.Model):
    rowid_num_aquisicion = models.OneToOneField('SbTabAcervo', models.DO_NOTHING, db_column='rowid_num_aquisicion', primary_key=True)
    rowid_car = models.ForeignKey('SeCatEmpleado', models.DO_NOTHING, db_column='rowid_car')
    rowid_empleado = models.IntegerField()
    feci_pres_emp = models.DateField()
    fecf_pre_emp = models.DateField(blank=True, null=True)
    can_pres_emp = models.IntegerField(blank=True, null=True)
    ti_mov_pres_emp = models.CharField(max_length=1, blank=True, null=True)
    es_pres_emp = models.CharField(max_length=1, blank=True, null=True)
    operador_emp = models.IntegerField(blank=True, null=True)
    fecha_real_emp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_pro_mov_emp_libros'
        unique_together = (('rowid_num_aquisicion', 'rowid_car', 'rowid_empleado', 'feci_pres_emp'), ('rowid_num_aquisicion', 'rowid_car', 'rowid_empleado', 'feci_pres_emp'),)


class SbProMovEstLibros(models.Model):
    fecha_ini_pres = models.DateField(primary_key=True)
    rowid_num_aquisicion = models.ForeignKey('SbTabAcervo', models.DO_NOTHING, db_column='rowid_num_aquisicion', blank=True, null=True)
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    fecha_fin_pres = models.DateField(blank=True, null=True)
    cant_pres = models.IntegerField(blank=True, null=True)
    tipo_movi_pres = models.CharField(max_length=1, blank=True, null=True)
    estatus_movi_pres = models.CharField(max_length=1, blank=True, null=True)
    operador_est = models.IntegerField(blank=True, null=True)
    fecha_real_est = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_pro_mov_est_libros'


class SbProMovUserexLibros(models.Model):
    rowid_num_aquisicion = models.OneToOneField('SbTabAcervo', models.DO_NOTHING, db_column='rowid_num_aquisicion', primary_key=True)
    id_servicio_ext = models.ForeignKey('SeTabEstudianteExt', models.DO_NOTHING, db_column='id_servicio_ext')
    feci_pres_userex = models.DateField(blank=True, null=True)
    fecf_pres_userex = models.DateField(blank=True, null=True)
    cant_pres_userex = models.IntegerField(blank=True, null=True)
    ti_mov_pres_userex = models.CharField(db_column='ti_mov_pres__userex', max_length=1, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    es_mov_pres_userex = models.CharField(max_length=1, blank=True, null=True)
    operador_userex = models.IntegerField(blank=True, null=True)
    fecha_real_userex = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_pro_mov_userex_libros'
        unique_together = (('rowid_num_aquisicion', 'id_servicio_ext'), ('rowid_num_aquisicion', 'id_servicio_ext'),)


class SbProPlanEstudioBiblio(models.Model):
    titulo = models.CharField(max_length=170)
    id_uni = models.IntegerField()
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField()
    autor = models.CharField(max_length=150)
    pais = models.CharField(max_length=50, blank=True, null=True)
    editorial = models.CharField(max_length=100)
    anio_sol = models.IntegerField(blank=True, null=True)
    no_ejemp = models.IntegerField(blank=True, null=True)
    ed = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    solicitados = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    estatus = models.CharField(max_length=2, blank=True, null=True)
    cve_donacion = models.IntegerField(primary_key=True)
    isbn = models.CharField(max_length=50)
    anio_alta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sb_pro_plan_estudio_biblio'


class SbSeguimientoMultas(models.Model):
    folio_sm = models.FloatField(primary_key=True)
    id_tipo_pag = models.IntegerField(blank=True, null=True)
    folio_rec = models.FloatField(blank=True, null=True)
    fecha_pag_bib = models.DateField(blank=True, null=True)
    id_matricula = models.FloatField(blank=True, null=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    id_empleado = models.IntegerField(blank=True, null=True)
    id_servicio_ext = models.FloatField(blank=True, null=True)
    saldo_multa = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usuario_movimineto = models.FloatField(blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)
    estatus_movimiento = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_seguimiento_multas'


class SbTabAcervo(models.Model):
    rowid_num_aquisicion = models.IntegerField(primary_key=True)
    rowid_ficha = models.ForeignKey(SbCatLibros, models.DO_NOTHING, db_column='rowid_ficha', blank=True, null=True)
    num_adquisicion = models.FloatField()
    ejemplar_acervo = models.IntegerField(blank=True, null=True)
    volumen_acervo = models.IntegerField(blank=True, null=True)
    estatus_acervo = models.CharField(max_length=1, blank=True, null=True)
    estatus_prestamo = models.CharField(max_length=1, blank=True, null=True)
    tomo_acervo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_acervo'


class SbTabAdquisicion(models.Model):
    rowid_aquisicion = models.IntegerField(primary_key=True)
    rowid_editorial = models.ForeignKey(SbCatEditorial, models.DO_NOTHING, db_column='rowid_editorial', blank=True, null=True)
    rowid_area_cono = models.ForeignKey(SbCatAreasConocimiento, models.DO_NOTHING, db_column='rowid_area_cono', blank=True, null=True)
    id_adquisicion = models.FloatField()
    titulo_adqui = models.CharField(max_length=255, blank=True, null=True)
    autor_adqui = models.CharField(max_length=60, blank=True, null=True)
    edicion_adqui = models.CharField(max_length=20, blank=True, null=True)
    fecha_adqui = models.DateField(blank=True, null=True)
    isbn_adqui = models.CharField(max_length=40, blank=True, null=True)
    ejemplares_soli = models.IntegerField(blank=True, null=True)
    ejemplares_surt = models.IntegerField(blank=True, null=True)
    no_factura = models.FloatField(blank=True, null=True)
    costo_adqui = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_rece = models.DateField(blank=True, null=True)
    estatus_adqui = models.CharField(max_length=1, blank=True, null=True)
    numeros_adq = models.CharField(max_length=255, blank=True, null=True)
    estatus_mat = models.CharField(max_length=1, blank=True, null=True)
    id_div_cono = models.IntegerField(blank=True, null=True)
    descri_larga_asi_adq = models.CharField(max_length=50, blank=True, null=True)
    volumen_adqui = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_adquisicion'


class SbTabConstanciaNoAdeudo(models.Model):
    num_noadeudo = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey('SeCatEmpleado', models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_empleado = models.IntegerField(blank=True, null=True)
    id_servicio_ext = models.ForeignKey('SeTabEstudianteExt', models.DO_NOTHING, db_column='id_servicio_ext', blank=True, null=True)
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    fecha_na = models.DateField()
    usuario_impna = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sb_tab_constancia_no_adeudo'


class SbTabDonacion(models.Model):
    rowid_donacion = models.IntegerField(primary_key=True)
    rowid_editorial = models.ForeignKey(SbCatEditorial, models.DO_NOTHING, db_column='rowid_editorial', blank=True, null=True)
    rowid_area_cono = models.ForeignKey(SbCatAreasConocimiento, models.DO_NOTHING, db_column='rowid_area_cono', blank=True, null=True)
    id_donacion = models.IntegerField()
    titulo_dona = models.CharField(max_length=255, blank=True, null=True)
    autor_dona = models.CharField(max_length=60, blank=True, null=True)
    edicion_dona = models.CharField(max_length=20, blank=True, null=True)
    ejemplares_dona = models.IntegerField(blank=True, null=True)
    fecha_dona = models.DateField(blank=True, null=True)
    nom_donador = models.CharField(max_length=60, blank=True, null=True)
    estatus_dona = models.CharField(max_length=1, blank=True, null=True)
    num_ficha_dona = models.FloatField(blank=True, null=True)
    volumen_dona = models.IntegerField(blank=True, null=True)
    id_div_dona = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_donacion'


class SbTabDonacionEstudiante(models.Model):
    cve_donacion = models.IntegerField(primary_key=True)
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    fecha_donacion = models.DateField(blank=True, null=True)
    estatus = models.CharField(max_length=5, blank=True, null=True)
    empleadorecibio = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_donacion_estudiante'


class SbTabEstaBib(models.Model):
    id_conse_bib = models.IntegerField(primary_key=True)
    num_ficha_bib = models.FloatField()
    id_div_bib = models.IntegerField(blank=True, null=True)
    fecha_entrada_bib = models.DateField(blank=True, null=True)
    estatus_mat_bib = models.CharField(max_length=1, blank=True, null=True)
    estatus_adqui_bib = models.CharField(max_length=1, blank=True, null=True)
    num_sem = models.IntegerField(blank=True, null=True)
    titulo_adqui_bib = models.IntegerField(blank=True, null=True)
    volumen_adqui_bib = models.IntegerField(blank=True, null=True)
    id_area_cono_bib = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_esta_bib'
        unique_together = (('id_conse_bib', 'num_ficha_bib'), ('id_conse_bib', 'num_ficha_bib'),)


class SbTabEtiquetas(models.Model):
    rowid_etiqueta = models.IntegerField(primary_key=True)
    id_etiqueta = models.CharField(max_length=5)
    indicador = models.CharField(max_length=3)
    descri_etiqueta = models.CharField(max_length=60, blank=True, null=True)
    estatus_etiqueta = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_etiquetas'


class SbTabPagosBiblioteca(models.Model):
    rowid_tipo_pag = models.OneToOneField('SeCatTipoPago', models.DO_NOTHING, db_column='rowid_tipo_pag', primary_key=True)
    folio_rec = models.FloatField()
    fecha_pag_bib = models.DateField()
    rowid_car = models.ForeignKey('SeCatEmpleado', models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_empleado = models.IntegerField(blank=True, null=True)
    id_servicio_ext = models.ForeignKey('SeTabEstudianteExt', models.DO_NOTHING, db_column='id_servicio_ext', blank=True, null=True)
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    importe_mul = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estatus_pag_bib = models.CharField(max_length=1, blank=True, null=True)
    usuario_cobro = models.CharField(max_length=10, blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    num_ficha_pag_bib = models.FloatField(blank=True, null=True)
    num_recibo = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)
    fechamodifica = models.DateField(blank=True, null=True)
    importemodifica = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    razonmodifica = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_pagos_biblioteca'
        unique_together = (('rowid_tipo_pag', 'folio_rec', 'fecha_pag_bib'), ('rowid_tipo_pag', 'folio_rec', 'fecha_pag_bib'),)


class SbTabParBiblio(models.Model):
    id_serv = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    max_dias = models.IntegerField(blank=True, null=True)
    max_libros = models.IntegerField(blank=True, null=True)
    mul_dia = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    mul_hora = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    hora_sal = models.TimeField(blank=True, null=True)
    hora_ent = models.TimeField(blank=True, null=True)
    fecha_ini_par_bib = models.DateField(blank=True, null=True)
    fecha_fin_par_bib = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_par_biblio'


class SbTabSolicitud(models.Model):
    id_solicitud = models.IntegerField(primary_key=True)
    id_conse_sol = models.IntegerField()
    rowid_editorial = models.ForeignKey(SbCatEditorial, models.DO_NOTHING, db_column='rowid_editorial', blank=True, null=True)
    rowid_car = models.ForeignKey('SeCatEmpleado', models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_empleado = models.IntegerField(blank=True, null=True)
    autor_sol = models.CharField(max_length=255, blank=True, null=True)
    titulo_sol = models.CharField(max_length=255, blank=True, null=True)
    edicion_sol = models.CharField(max_length=20, blank=True, null=True)
    ejemplares_sol = models.IntegerField(blank=True, null=True)
    fecha_sol = models.DateField(blank=True, null=True)
    estatus_sol = models.CharField(max_length=1, blank=True, null=True)
    descri_larga_asi_sol = models.CharField(max_length=50, blank=True, null=True)
    volumen_sol = models.IntegerField(blank=True, null=True)
    estatus_mat_sol = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_tab_solicitud'
        unique_together = (('id_solicitud', 'id_conse_sol'), ('id_solicitud', 'id_conse_sol'),)


class SeAcuEstudiante(models.Model):
    anio_acu_est = models.IntegerField(primary_key=True)
    periodo_acu_est = models.IntegerField()
    evento_acu_est = models.CharField(max_length=3)
    clave_acu_est = models.IntegerField()
    generacion_acu_est = models.IntegerField()
    rowid_car = models.ForeignKey('SeCatCarrera', models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_grado = models.ForeignKey('SeCatGrado', models.DO_NOTHING, db_column='rowid_grado', blank=True, null=True)
    porcentaje_acu_est = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total_acu_est = models.IntegerField(blank=True, null=True)
    descri_corto_acu_est = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_acu_estudiante'
        unique_together = (('anio_acu_est', 'periodo_acu_est', 'evento_acu_est', 'clave_acu_est', 'generacion_acu_est'), ('anio_acu_est', 'periodo_acu_est', 'evento_acu_est', 'clave_acu_est', 'generacion_acu_est'),)


class SeAcuPeriodos(models.Model):
    rowid_acu = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey('SeCatCarrera', models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    anio_acu = models.IntegerField()
    periodo_acu = models.IntegerField()
    evento_acu = models.CharField(max_length=3)
    clave_acu = models.IntegerField()
    generacion_acu = models.IntegerField()
    rondas_acu = models.IntegerField()
    total_acu = models.IntegerField(blank=True, null=True)
    descri_corto_acu = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_acu_periodos'


class SeCatActa(models.Model):
    id_uni = models.IntegerField(primary_key=True)
    id_div = models.IntegerField()
    id_car = models.IntegerField()
    id_folio = models.IntegerField()
    matricula_act = models.FloatField()
    nombre_act = models.CharField(max_length=80)
    fecha_act = models.DateField()
    usuario_alta = models.CharField(max_length=10, blank=True, null=True)
    nombre_usuario_que_imprimio = models.CharField(max_length=80, blank=True, null=True)
    libro_acta = models.CharField(max_length=10, blank=True, null=True)
    fojas_acta = models.CharField(max_length=10, blank=True, null=True)
    nombre_esta = models.CharField(max_length=1000, blank=True, null=True)
    no_imp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_acta'
        unique_together = (('id_uni', 'id_div', 'id_car', 'id_folio'), ('id_uni', 'id_div', 'id_car', 'id_folio'),)


class SeCatActividades(models.Model):
    rowid_actividad = models.IntegerField(primary_key=True)
    id_actividad = models.IntegerField()
    descri_corto_act = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_act = models.CharField(max_length=50, blank=True, null=True)
    estatus_act = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_actividades'


class SeCatAreaBachillerato(models.Model):
    rowid_area_bac = models.IntegerField(primary_key=True)
    id_area_bac = models.IntegerField()
    descri_larga_bac = models.CharField(max_length=50)
    descri_corta_bac = models.CharField(max_length=10)
    estatus_bac = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_area_bachillerato'


class SeCatAreas(models.Model):
    rowid_area = models.IntegerField(primary_key=True)
    rowid_empresa = models.ForeignKey('SeCatEmpresas', models.DO_NOTHING, db_column='rowid_empresa', blank=True, null=True)
    id_area = models.IntegerField()
    descri_larga_area = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_area = models.CharField(max_length=10, blank=True, null=True)
    estatus_area = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_areas'


class SeCatAsignatura(models.Model):
    rowid_asignatura = models.IntegerField(primary_key=True)
    rowid_plan_est = models.ForeignKey('SeCatPlaEstudio', models.DO_NOTHING, db_column='rowid_plan_est', blank=True, null=True)
    rowid_car = models.ForeignKey('SeCatCarrera', models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    id_asignatura = models.CharField(max_length=20)
    descri_larga_asi = models.CharField(max_length=80)
    descri_corto_asi = models.CharField(max_length=10)
    estatus_asi = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_asignatura'


class SeCatBecas(models.Model):
    rowid_becas = models.IntegerField(primary_key=True)
    id_becas = models.IntegerField()
    valor_ini_bec = models.DecimalField(max_digits=6, decimal_places=2)
    valor_fin_bec = models.DecimalField(max_digits=6, decimal_places=2)
    porcentaje_beca = models.DecimalField(max_digits=6, decimal_places=2)
    estatus_bec = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_becas'


class SeCatCarrera(models.Model):
    rowid_car = models.IntegerField(primary_key=True)
    rowid_div = models.ForeignKey('SeCatDivision', models.DO_NOTHING, db_column='rowid_div', blank=True, null=True)
    id_car = models.IntegerField()
    descri_largo_car = models.CharField(max_length=50)
    descri_corto_car = models.CharField(max_length=10)
    estatus_car = models.CharField(max_length=1, blank=True, null=True)
    ceneval_car = models.CharField(max_length=1, blank=True, null=True)
    descri_largo_tit = models.CharField(max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_carrera'


class SeCatClinica(models.Model):
    rowid_cli = models.IntegerField(primary_key=True)
    rowid_col = models.ForeignKey('SeCatColonia', models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    id_clinica = models.CharField(max_length=5)
    descri_larga_cli = models.CharField(max_length=50, blank=True, null=True)
    descri_corta_cli = models.CharField(max_length=10, blank=True, null=True)
    direcc_cli = models.CharField(max_length=60, blank=True, null=True)
    rfc_cli = models.CharField(max_length=15, blank=True, null=True)
    tel1_cli = models.CharField(max_length=15, blank=True, null=True)
    tel2_cli = models.CharField(max_length=15, blank=True, null=True)
    fax1_cli = models.CharField(max_length=15, blank=True, null=True)
    email_cli = models.CharField(max_length=40, blank=True, null=True)
    codpclini = models.IntegerField(blank=True, null=True)
    estatus_clini = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_clinica'


class SeCatColonia(models.Model):
    rowid_col = models.IntegerField(primary_key=True)
    rowid_mundel = models.ForeignKey('SeCatMunicipioDelegacion', models.DO_NOTHING, db_column='rowid_mundel', blank=True, null=True)
    id_col = models.IntegerField()
    descri_largo_col = models.CharField(max_length=50)
    descrip_corto_col = models.CharField(max_length=10)
    estatus_col = models.CharField(max_length=1, blank=True, null=True)
    codposcol = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_colonia'


class SeCatDepartamentos(models.Model):
    rowid_area = models.OneToOneField(SeCatAreas, models.DO_NOTHING, db_column='rowid_area', primary_key=True)
    rowid_departamento = models.IntegerField()
    id_departamento = models.IntegerField()
    descri_largo_dep = models.CharField(max_length=100, blank=True, null=True)
    descri_corto_dep = models.CharField(max_length=10, blank=True, null=True)
    estatus_dep = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_departamentos'
        unique_together = (('rowid_area', 'rowid_departamento'), ('rowid_area', 'rowid_departamento'),)


class SeCatDeptoEmp(models.Model):
    rowid_depto = models.IntegerField(primary_key=True)
    id_depto = models.CharField(max_length=3)
    conse_depto = models.IntegerField()
    descri_corto_dep_emp = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_dep_emp = models.CharField(max_length=50, blank=True, null=True)
    titular_depto = models.CharField(max_length=60, blank=True, null=True)
    clave_ser = models.IntegerField(blank=True, null=True)
    estatus_depto = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_depto_emp'


class SeCatDivision(models.Model):
    rowid_div = models.IntegerField(primary_key=True)
    rowid_uni = models.ForeignKey('SeCatUniversidad', models.DO_NOTHING, db_column='rowid_uni', blank=True, null=True)
    id_div = models.IntegerField()
    descri_larga_div = models.CharField(max_length=50)
    descri_corta_div = models.CharField(max_length=10)
    representante_div = models.CharField(max_length=50)
    telefono_1_div = models.CharField(max_length=15, blank=True, null=True)
    telefono_2_div = models.CharField(max_length=15, blank=True, null=True)
    extension1_div = models.CharField(max_length=7, blank=True, null=True)
    extension2_div = models.CharField(max_length=7, blank=True, null=True)
    mail_div = models.CharField(max_length=25, blank=True, null=True)
    estatus_div = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_division'


class SeCatDocumentacion(models.Model):
    rowid_doc = models.IntegerField(primary_key=True)
    id_doc = models.IntegerField()
    descri_corto_doc = models.CharField(max_length=10)
    descri_largo_doc = models.CharField(max_length=200)
    importante_doc = models.CharField(max_length=1)
    cve_control_doc = models.CharField(max_length=4)
    estatus_grado = models.CharField(max_length=15, blank=True, null=True)
    estatus_doc = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_documentacion'


class SeCatEmpleado(models.Model):
    rowid_car = models.OneToOneField(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    rowid_empleado = models.IntegerField()
    rowid_academico = models.ForeignKey('SeCatNivelAcademico', models.DO_NOTHING, db_column='rowid_academico', blank=True, null=True)
    rowid_depto = models.ForeignKey(SeCatDeptoEmp, models.DO_NOTHING, db_column='rowid_depto', blank=True, null=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    rowid_puesto = models.ForeignKey('SeCatSueldos', models.DO_NOTHING, db_column='rowid_puesto', blank=True, null=True)
    rowid_sueldo = models.IntegerField(blank=True, null=True)
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
    estatus_emp = models.CharField(max_length=1, blank=True, null=True)
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
    id_edo_nac_emp = models.IntegerField(blank=True, null=True)
    estatus_biblio = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_empleado'
        unique_together = (('rowid_car', 'rowid_empleado'), ('rowid_car', 'rowid_empleado'),)


class SeCatEmpresas(models.Model):
    rowid_empresa = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    rowid_giro = models.ForeignKey('SeCatSubgiros', models.DO_NOTHING, db_column='rowid_giro', blank=True, null=True)
    rowid_subgiro = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField()
    razon_social_cia = models.CharField(max_length=300)
    direccion_cia = models.CharField(max_length=500, blank=True, null=True)
    rfc_cia = models.CharField(max_length=15, blank=True, null=True)
    codpos_cia = models.IntegerField(blank=True, null=True)
    telefono1_cia = models.CharField(max_length=15, blank=True, null=True)
    telefono2_cia = models.CharField(max_length=15, blank=True, null=True)
    telefono3_cia = models.CharField(max_length=15, blank=True, null=True)
    fax1_cia = models.CharField(max_length=15, blank=True, null=True)
    fax2_cia = models.CharField(max_length=15, blank=True, null=True)
    fax3_cia = models.CharField(max_length=15, blank=True, null=True)
    ext1_cia = models.CharField(max_length=7, blank=True, null=True)
    ext2_cia = models.CharField(max_length=7, blank=True, null=True)
    ext3_cia = models.CharField(max_length=7, blank=True, null=True)
    mail_cia = models.CharField(max_length=100, blank=True, null=True)
    pagina_internet_cia = models.CharField(max_length=35, blank=True, null=True)
    estatus_cia = models.CharField(max_length=1, blank=True, null=True)
    representante_legal = models.CharField(max_length=250, blank=True, null=True)
    tipo_empresa = models.CharField(max_length=3, blank=True, null=True)
    tamanio_emp = models.CharField(max_length=3, blank=True, null=True)
    sector_emp = models.CharField(max_length=3, blank=True, null=True)
    caracter = models.CharField(max_length=3, blank=True, null=True)
    cargo_rep = models.CharField(max_length=500, blank=True, null=True)
    rama_em = models.CharField(max_length=200, blank=True, null=True)
    id_programa = models.IntegerField(blank=True, null=True)
    vigencia = models.CharField(max_length=100, blank=True, null=True)
    tipovinculacion = models.CharField(max_length=25, blank=True, null=True)
    facebook = models.CharField(max_length=30, blank=True, null=True)
    twitter = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_empresas'


class SeCatEstado(models.Model):
    rowid_edo = models.IntegerField(primary_key=True)
    rowid_pais = models.ForeignKey('SeCatPais', models.DO_NOTHING, db_column='rowid_pais', blank=True, null=True)
    id_edo = models.IntegerField()
    descri_largo_edo = models.CharField(max_length=50)
    descri_corto_edo = models.CharField(max_length=10)
    estatus_edo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_estado'


class SeCatEstatusEstudiante(models.Model):
    rowid_evnto_est = models.IntegerField(primary_key=True)
    id_evento_est = models.CharField(max_length=3)
    consecutivo_est = models.IntegerField()
    descri_largo_tipo_est = models.CharField(max_length=50)
    descri_corto_tipo_est = models.CharField(max_length=10)
    estatus_tipo_est = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_estatus_estudiante'


class SeCatEstatusTitulado(models.Model):
    id_estatus_tit = models.IntegerField(primary_key=True)
    descri_lar_estatus = models.CharField(max_length=300, blank=True, null=True)
    descri_cor_estatus = models.CharField(max_length=75, blank=True, null=True)
    estatus = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_estatus_titulado'


class SeCatFechas(models.Model):
    rowid_fecha_asi = models.IntegerField(primary_key=True)
    fecha_asi = models.DateField()
    diajul = models.IntegerField(blank=True, null=True)
    cvedia = models.CharField(max_length=2, blank=True, null=True)
    numdia = models.IntegerField(blank=True, null=True)
    numsem = models.IntegerField(blank=True, null=True)
    diash = models.CharField(max_length=1, blank=True, null=True)
    periodo_fechas = models.IntegerField(blank=True, null=True)
    estatus_fechas = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_fechas'


class SeCatFechasImss(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    fecha_ini_registro = models.DateField(blank=True, null=True)
    fecha_fin_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_fechas_imss'


class SeCatFechasServicio(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    fecha_ini_registro = models.DateField(blank=True, null=True)
    fecha_fin_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_fechas_servicio'


class SeCatFoliosImpresion(models.Model):
    rowid_num_folio = models.IntegerField(primary_key=True)
    num_folio = models.FloatField()
    est_folio_imp = models.CharField(max_length=1, blank=True, null=True)
    nombre_user = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_folios_impresion'


class SeCatGeneral(models.Model):
    rowid_general = models.IntegerField(primary_key=True)
    id_general = models.CharField(max_length=10)
    numero_gral = models.IntegerField()
    des_corto_gral = models.CharField(max_length=10, blank=True, null=True)
    des_largo_gral = models.CharField(max_length=255, blank=True, null=True)
    estatus_gral = models.CharField(max_length=1, blank=True, null=True)
    especificacion_gral = models.CharField(max_length=255, blank=True, null=True)
    activo_general = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_general'


class SeCatGiros(models.Model):
    rowid_giro = models.IntegerField(primary_key=True)
    id_giro = models.IntegerField()
    descri_largo_gir = models.CharField(max_length=100)
    descri_corto_gir = models.CharField(max_length=10)
    estatus_gir = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_giros'


class SeCatGrado(models.Model):
    rowid_grado = models.IntegerField(primary_key=True)
    id_grado = models.IntegerField()
    descri_corto_gra = models.CharField(max_length=10)
    estatus_gra = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_grado'


class SeCatGrupo(models.Model):
    rowid_grupo = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_grado = models.ForeignKey(SeCatGrado, models.DO_NOTHING, db_column='rowid_grado', blank=True, null=True)
    id_grupo = models.IntegerField()
    descri_largo_gpo = models.CharField(max_length=60)
    descri_corto_gpo = models.CharField(max_length=10)
    estatus_gpo = models.CharField(max_length=1, blank=True, null=True)
    lim_gpo = models.IntegerField(blank=True, null=True)
    lim_rec_gpo = models.IntegerField(blank=True, null=True)
    lim_acu_gpo = models.IntegerField(blank=True, null=True)
    lim_acu_rec_gpo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_grupo'


class SeCatIndicador(models.Model):
    rowid_indicador = models.IntegerField(primary_key=True)
    id_indicador = models.IntegerField()
    descri_largo_ind = models.CharField(max_length=50)
    descri_corto_ind = models.CharField(max_length=10)
    estatus_ind = models.CharField(max_length=1, blank=True, null=True)
    cve_control_ind = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'se_cat_indicador'


class SeCatInstitucion(models.Model):
    rowid_institucion = models.IntegerField(primary_key=True)
    id_institucion = models.IntegerField()
    descri_corto_ins = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_ins = models.CharField(max_length=50, blank=True, null=True)
    estatus_ins = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_institucion'


class SeCatMaterialLaboratorio(models.Model):
    id_mat_lab = models.FloatField(primary_key=True)
    descri_largo_mat = models.CharField(max_length=100)
    descri_corto_mat = models.CharField(max_length=50)
    estatus_mat_lab = models.CharField(max_length=10, blank=True, null=True)
    estatus_mov_deuda = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_material_laboratorio'


class SeCatMedioDifusion(models.Model):
    rowid_medio_dif = models.IntegerField(primary_key=True)
    id_medio_dif = models.IntegerField()
    descri_largo_meddif = models.CharField(max_length=50)
    descri_corto_meddif = models.CharField(max_length=10)
    estatus_dif = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_medio_difusion'


class SeCatMunicipioDelegacion(models.Model):
    rowid_mundel = models.IntegerField(primary_key=True)
    rowid_edo = models.ForeignKey(SeCatEstado, models.DO_NOTHING, db_column='rowid_edo', blank=True, null=True)
    id_mundel = models.IntegerField()
    descri_largo_mundel = models.CharField(max_length=50)
    descri_corto_mundel = models.CharField(max_length=10)
    estatus_mundel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_municipio_delegacion'


class SeCatNivelAcademico(models.Model):
    rowid_academico = models.IntegerField(primary_key=True)
    id_academico = models.IntegerField()
    descri_largo_acade = models.CharField(max_length=50)
    descri_corto_acade = models.CharField(max_length=10)
    estatus_acade = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_nivel_academico'


class SeCatNumeroRecibos(models.Model):
    id_recibo = models.FloatField(primary_key=True)
    est_imp_recibo = models.CharField(max_length=1, blank=True, null=True)
    nom_user_recibo = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_numero_recibos'


class SeCatPais(models.Model):
    rowid_pais = models.IntegerField(primary_key=True)
    id_pais = models.IntegerField(blank=True, null=True)
    descri_largo_pais = models.CharField(max_length=50, blank=True, null=True)
    descri_corto_pais = models.CharField(max_length=10, blank=True, null=True)
    estatus_pais = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_pais'


class SeCatPeriodos(models.Model):
    rowid_per = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    evento_per = models.CharField(max_length=3)
    consecutivo_per = models.IntegerField()
    fecha_inicial_per = models.DateField(blank=True, null=True)
    fecha_final_per = models.DateField(blank=True, null=True)
    anio_per = models.IntegerField(blank=True, null=True)
    periodo_per = models.IntegerField(blank=True, null=True)
    descripcion_per = models.CharField(max_length=255, blank=True, null=True)
    estatus_per = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_periodos'


class SeCatPersonal(models.Model):
    id_trabajador = models.IntegerField(primary_key=True)
    rowid_area = models.ForeignKey(SeCatDepartamentos, models.DO_NOTHING, db_column='rowid_area', blank=True, null=True)
    rowid_departamento = models.IntegerField(blank=True, null=True)
    ap_tra = models.CharField(max_length=30, blank=True, null=True)
    am_tra = models.CharField(max_length=30, blank=True, null=True)
    nombre_tra = models.CharField(max_length=40, blank=True, null=True)
    puesto_tra = models.CharField(max_length=50, blank=True, null=True)
    telefono_tra = models.CharField(max_length=15, blank=True, null=True)
    email_trab = models.CharField(max_length=40, blank=True, null=True)
    estatus_tra = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_personal'


class SeCatPlaEstudio(models.Model):
    rowid_plan_est = models.IntegerField(primary_key=True)
    id_plan_est = models.IntegerField()
    decri_larga_plan_est = models.CharField(max_length=50)
    descri_corta_plan_est = models.CharField(max_length=10)
    estatus_plan_est = models.CharField(max_length=1, blank=True, null=True)
    fec_alta_estpla = models.DateField(blank=True, null=True)
    user_alta_estpla = models.CharField(max_length=10, blank=True, null=True)
    fec_baja_estpla = models.DateField(blank=True, null=True)
    user_baja_estpla = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_pla_estudio'


class SeCatPlaza(models.Model):
    rowid_plaza = models.IntegerField(primary_key=True)
    id_plaza = models.IntegerField()
    descri_corto_plaza = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_plaza = models.CharField(max_length=50, blank=True, null=True)
    estatus_plaza = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_plaza'


class SeCatProfesorHorario(models.Model):
    dia_sem_hor = models.CharField(primary_key=True, max_length=2)
    estatus_hor = models.CharField(max_length=3)
    id_grupo = models.IntegerField()
    id_empleado = models.IntegerField()
    periodo_hor = models.IntegerField()
    rowid_asignatura = models.ForeignKey('SeProGpoAsig', models.DO_NOTHING, db_column='rowid_asignatura', blank=True, null=True)
    rowid_pro_gpo_asig = models.IntegerField(blank=True, null=True)
    rowid_car = models.ForeignKey('SeCatSalones', models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_salon = models.IntegerField(blank=True, null=True)
    rowid_actividad = models.ForeignKey(SeCatActividades, models.DO_NOTHING, db_column='rowid_actividad', blank=True, null=True)
    entrada_hor = models.DecimalField(max_digits=5, decimal_places=2)
    salida_hor = models.DecimalField(max_digits=5, decimal_places=2)
    total_hor = models.DecimalField(max_digits=5, decimal_places=2)
    horas_asig = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    horas_restan = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_profesor_horario'
        unique_together = (('dia_sem_hor', 'estatus_hor', 'id_grupo', 'id_empleado', 'periodo_hor'), ('dia_sem_hor', 'estatus_hor', 'id_grupo', 'id_empleado', 'periodo_hor'),)


class SeCatPrograma(models.Model):
    id_programa = models.IntegerField(primary_key=True)
    descri_larga_programa = models.CharField(max_length=150, blank=True, null=True)
    descri_corta_programa = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_programa'


class SeCatProyectos(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    id_trabajador = models.ForeignKey(SeCatPersonal, models.DO_NOTHING, db_column='id_trabajador', blank=True, null=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    nombre_proy = models.CharField(max_length=255)
    descri_corto_proy = models.CharField(max_length=10)
    estatus_proy = models.CharField(max_length=1, blank=True, null=True)
    objetivo_proy = models.CharField(max_length=500, blank=True, null=True)
    producto_proy = models.CharField(max_length=500, blank=True, null=True)
    anio_proy = models.IntegerField(blank=True, null=True)
    periodo_proy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_proyectos'


class SeCatRama(models.Model):
    id_rama = models.IntegerField(primary_key=True)
    descri_larga_rama = models.CharField(max_length=150, blank=True, null=True)
    descri_corta_rama = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_rama'


class SeCatSalones(models.Model):
    rowid_car = models.OneToOneField(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    rowid_salon = models.IntegerField()
    id_salon = models.IntegerField()
    descri_corto_salon = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_salon = models.CharField(max_length=50, blank=True, null=True)
    estatus_salon = models.CharField(max_length=1, blank=True, null=True)
    tipo_salon = models.CharField(max_length=3, blank=True, null=True)
    compartido_salon = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_salones'
        unique_together = (('rowid_car', 'rowid_salon'), ('rowid_car', 'rowid_salon'),)


class SeCatSector(models.Model):
    id_sector = models.IntegerField(primary_key=True)
    descri_larga_sector = models.CharField(max_length=150, blank=True, null=True)
    descri_corto_sector = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_sector'


class SeCatSubgiros(models.Model):
    rowid_giro = models.OneToOneField(SeCatGiros, models.DO_NOTHING, db_column='rowid_giro', primary_key=True)
    rowid_subgiro = models.IntegerField()
    id_subgiro = models.IntegerField()
    descri_largo_subgiro = models.CharField(max_length=100)
    descri_corto_subgiro = models.CharField(max_length=10)
    estatus_subgiro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_subgiros'
        unique_together = (('rowid_giro', 'rowid_subgiro'), ('rowid_giro', 'rowid_subgiro'),)


class SeCatSueldos(models.Model):
    rowid_puesto = models.OneToOneField('SeCatTipoPuesto', models.DO_NOTHING, db_column='rowid_puesto', primary_key=True)
    rowid_sueldo = models.IntegerField()
    id_sueldo = models.IntegerField()
    sueldo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_sueldos'
        unique_together = (('rowid_puesto', 'rowid_sueldo'), ('rowid_puesto', 'rowid_sueldo'),)


class SeCatTipoBajas(models.Model):
    rowid_tipo_baj = models.IntegerField(primary_key=True)
    id_tipo_baj = models.IntegerField()
    descri_largo_tipo_baj = models.CharField(max_length=50)
    descri_corto_tipo_baj = models.CharField(max_length=10)
    estatus_tipo_baj = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_tipo_bajas'


class SeCatTipoCambio(models.Model):
    rowid_tipo_cambio = models.IntegerField(primary_key=True)
    id_tipo_cambio = models.IntegerField()
    descri_tipocambio = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_tipo_cambio'


class SeCatTipoEscuela(models.Model):
    rowid_tipo_esc = models.IntegerField(primary_key=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    id_tipo_esc = models.IntegerField()
    descri_largo_esc = models.CharField(max_length=50)
    descri_corta_esc = models.CharField(max_length=10)
    estatus_esc = models.CharField(max_length=1, blank=True, null=True)
    institucion = models.CharField(max_length=50, blank=True, null=True)
    nombre_plantel = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_tipo_escuela'


class SeCatTipoPago(models.Model):
    rowid_tipo_pag = models.IntegerField(primary_key=True)
    id_tipo_pag = models.IntegerField()
    descri_largo_tip = models.CharField(max_length=50)
    descri_corto_tip = models.CharField(max_length=10)
    importe_total_tip = models.DecimalField(max_digits=15, decimal_places=2)
    estatus_tip = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_tipo_pago'


class SeCatTipoPuesto(models.Model):
    rowid_puesto = models.IntegerField(primary_key=True)
    rowid_plaza = models.ForeignKey(SeCatPlaza, models.DO_NOTHING, db_column='rowid_plaza', blank=True, null=True)
    id_puesto = models.IntegerField()
    descri_largo_pue = models.CharField(max_length=50)
    descri_corto_pue = models.CharField(max_length=10)
    estatus_pue = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_tipo_puesto'


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
    fax1_uni = models.CharField(max_length=15, blank=True, null=True)
    fax2_uni = models.CharField(max_length=15, blank=True, null=True)
    fax3_uni = models.CharField(max_length=15, blank=True, null=True)
    ext1_uni = models.CharField(max_length=7, blank=True, null=True)
    ext2_uni = models.CharField(max_length=7, blank=True, null=True)
    ext3_uni = models.CharField(max_length=7, blank=True, null=True)
    mail_uni = models.CharField(max_length=30, blank=True, null=True)
    pagina_internet_uni = models.CharField(max_length=35, blank=True, null=True)
    contacto_uni = models.CharField(max_length=50)
    estatus_uni = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_cat_universidad'


class SeParTipoConsecutivo(models.Model):
    rowid_tipo_par = models.IntegerField(primary_key=True)
    rowid_div = models.ForeignKey(SeCatDivision, models.DO_NOTHING, db_column='rowid_div', blank=True, null=True)
    id_tipo_par = models.IntegerField()
    nombre_tabla = models.CharField(max_length=60, blank=True, null=True)
    nombre_atributo = models.CharField(max_length=60, blank=True, null=True)
    num_conse_inicial = models.FloatField(blank=True, null=True)
    num_conse_final = models.FloatField(blank=True, null=True)
    estatus_par = models.CharField(max_length=1, blank=True, null=True)
    num_conse_actual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_par_tipo_consecutivo'


class SeProAsiIndicador(models.Model):
    rowid_pro_asi_ind = models.IntegerField(primary_key=True)
    rowid_pro_plan_est = models.ForeignKey('SeProPlanEstudio', models.DO_NOTHING, db_column='rowid_pro_plan_est', blank=True, null=True)
    rowid_indicador = models.ForeignKey(SeCatIndicador, models.DO_NOTHING, db_column='rowid_indicador', blank=True, null=True)
    porcentaje_pro_asi_idi = models.DecimalField(max_digits=5, decimal_places=2)
    comen_pro_asi_ind = models.CharField(max_length=30, blank=True, null=True)
    estatus_peai = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_asi_indicador'


class SeProAsisTotal(models.Model):
    parcial_asi_tot = models.IntegerField(primary_key=True)
    rowid_asignatura = models.ForeignKey('SeProGpoAsig', models.DO_NOTHING, db_column='rowid_asignatura', blank=True, null=True)
    rowid_pro_gpo_asig = models.IntegerField(blank=True, null=True)
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    total_asis = models.IntegerField(blank=True, null=True)
    porcen_asisten = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_ultima_asi = models.DateField(blank=True, null=True)
    total_asi_prof = models.IntegerField(blank=True, null=True)
    fecha_alta_asi = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_asis_total'


class SeProAspDocu(models.Model):
    rowid_doc = models.ForeignKey(SeCatDocumentacion, models.DO_NOTHING, db_column='rowid_doc')
    rowid_car = models.OneToOneField('SeTabAspirante', models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    folio_utn_asp = models.CharField(max_length=20)
    import_doc = models.CharField(max_length=1)
    entrego_doc = models.CharField(max_length=1)
    comentario_doc = models.CharField(max_length=100, blank=True, null=True)
    fecha_alta_doc = models.DateField(blank=True, null=True)
    user_alta_doc = models.CharField(max_length=10, blank=True, null=True)
    fecha_baja_doc = models.DateField(blank=True, null=True)
    user_baja_doc = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_doc = models.DateField(blank=True, null=True)
    user_cambio_doc = models.CharField(max_length=10, blank=True, null=True)
    estatus_doc_aspi = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_asp_docu'
        unique_together = (('rowid_car', 'rowid_doc', 'folio_utn_asp'), ('rowid_car', 'rowid_doc', 'folio_utn_asp'),)


class SeProAspDocuHis(models.Model):
    id_uni_asp_his = models.OneToOneField('SeTabAspiranteHis', models.DO_NOTHING, db_column='id_uni_asp_his', primary_key=True)
    id_div_asp_his = models.IntegerField()
    id_car_asp_his = models.IntegerField()
    folio_utn_asp_his = models.CharField(max_length=20)
    id_doc_his = models.IntegerField()
    import_doc_his = models.CharField(max_length=1, blank=True, null=True)
    entrego_doc_his = models.CharField(max_length=1, blank=True, null=True)
    comentario_doc_his = models.CharField(max_length=100, blank=True, null=True)
    fecha_alta_doc_his = models.DateField(blank=True, null=True)
    user_alta_doc_his = models.CharField(max_length=10, blank=True, null=True)
    fecha_baja_doc_his = models.DateField(blank=True, null=True)
    user_baja_doc_his = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_doc_his = models.DateField(blank=True, null=True)
    user_cambio_doc_his = models.CharField(max_length=10, blank=True, null=True)
    estatus_doc_aspi_his = models.CharField(max_length=1, blank=True, null=True)
    periodo_doc_his = models.IntegerField(blank=True, null=True)
    anio_doc_his = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_asp_docu_his'
        unique_together = (('id_uni_asp_his', 'id_div_asp_his', 'id_car_asp_his', 'folio_utn_asp_his', 'id_doc_his'), ('id_uni_asp_his', 'id_div_asp_his', 'id_car_asp_his', 'folio_utn_asp_his', 'id_doc_his'),)


class SeProEgreDoc(models.Model):
    rowid_matricula_egre = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_doc = models.ForeignKey(SeCatDocumentacion, models.DO_NOTHING, db_column='rowid_doc', blank=True, null=True)
    id_matricula_egre = models.CharField(max_length=20)
    importante_doc_egre = models.CharField(max_length=1, blank=True, null=True)
    entrego_doc_egre = models.CharField(max_length=1, blank=True, null=True)
    fec_alta_egre = models.DateField(blank=True, null=True)
    usr_alta_egre = models.CharField(max_length=10, blank=True, null=True)
    comentario_doc_engre = models.CharField(max_length=100, blank=True, null=True)
    estado_doc_egre = models.CharField(max_length=1, blank=True, null=True)
    fec_baja_egre = models.DateField(blank=True, null=True)
    usr_baja_egre = models.CharField(max_length=10, blank=True, null=True)
    fec_cambio_egre = models.DateField(blank=True, null=True)
    usr_cambio_egre = models.CharField(max_length=10, blank=True, null=True)
    anio_utn = models.IntegerField(blank=True, null=True)
    periodo_utn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_egre_doc'


class SeProEgresadoEmpresa(models.Model):
    rowid_pro_egre_emp = models.IntegerField(primary_key=True)
    rowid_empresa = models.ForeignKey(SeCatEmpresas, models.DO_NOTHING, db_column='rowid_empresa', blank=True, null=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    id_matricula_egre = models.CharField(max_length=20)
    fecha_ini_emp_egre = models.DateField()
    fecha_fin_emp_egre = models.DateField(blank=True, null=True)
    estatus_emp_egre = models.CharField(max_length=1, blank=True, null=True)
    nombre_jefe_emp = models.CharField(max_length=250, blank=True, null=True)
    cargo_jefe = models.CharField(max_length=100, blank=True, null=True)
    telefono_jefe_egre = models.CharField(max_length=15, blank=True, null=True)
    extension_jefe_egre = models.CharField(max_length=5, blank=True, null=True)
    fax_jefe_egre = models.CharField(max_length=15, blank=True, null=True)
    mail_jefe_egre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_egresado_empresa'


class SeProEstDoc(models.Model):
    rowid_doc = models.OneToOneField(SeCatDocumentacion, models.DO_NOTHING, db_column='rowid_doc', primary_key=True)
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula')
    importe_doc_est = models.CharField(max_length=1)
    entrego_doc_est = models.CharField(max_length=1)
    fec_alta_doc_est = models.DateField(blank=True, null=True)
    usr_alta_doc_est = models.CharField(max_length=10, blank=True, null=True)
    fec_baja_doc_est = models.DateField(blank=True, null=True)
    usr_baja_doc_est = models.CharField(max_length=10, blank=True, null=True)
    fec_cambio_doc_est = models.DateField(blank=True, null=True)
    usr_cambio_doc_est = models.CharField(max_length=10, blank=True, null=True)
    comentario_doc_est = models.CharField(max_length=255, blank=True, null=True)
    estatus_doc_est = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_est_doc'
        unique_together = (('rowid_doc', 'id_matricula'), ('rowid_doc', 'id_matricula'),)


class SeProGpoAsig(models.Model):
    rowid_asignatura = models.OneToOneField(SeCatAsignatura, models.DO_NOTHING, db_column='rowid_asignatura', primary_key=True)
    rowid_pro_gpo_asig = models.IntegerField()
    rowid_car = models.ForeignKey(SeCatEmpleado, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_empleado = models.IntegerField(blank=True, null=True)
    rowid_grupo = models.ForeignKey(SeCatGrupo, models.DO_NOTHING, db_column='rowid_grupo', blank=True, null=True)
    periodo_hor = models.IntegerField()
    estatus_asignatura = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_gpo_asig'
        unique_together = (('rowid_asignatura', 'rowid_pro_gpo_asig'), ('rowid_asignatura', 'rowid_pro_gpo_asig'),)


class SeProGralEstudiante(models.Model):
    id_uni = models.IntegerField(primary_key=True)
    id_div = models.IntegerField()
    id_car = models.IntegerField()
    id_matricula_egre = models.CharField(max_length=20)
    rowid_general = models.ForeignKey(SeCatGeneral, models.DO_NOTHING, db_column='rowid_general', blank=True, null=True)
    tipo_cuest_egre = models.CharField(max_length=1, blank=True, null=True)
    orden_cuest_egre = models.IntegerField(blank=True, null=True)
    estatus_cuest_egre = models.CharField(max_length=1, blank=True, null=True)
    especificacion_cuest = models.CharField(max_length=1, blank=True, null=True)
    empresa_egre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_gral_estudiante'
        unique_together = (('id_uni', 'id_div', 'id_car', 'id_matricula_egre'), ('id_uni', 'id_div', 'id_car', 'id_matricula_egre'),)


class SeProHorasServicio(models.Model):
    servicio = models.OneToOneField('SeTabEstudianteServicio', models.DO_NOTHING, primary_key=True)
    fecha_hor_ser = models.DateField()
    hora_ent_ser = models.TimeField()
    hora_sal_ser = models.TimeField(blank=True, null=True)
    estatus_hor_ser = models.CharField(max_length=1, blank=True, null=True)
    total_hor_ser = models.TimeField(blank=True, null=True)
    tipo_hor_ser = models.CharField(max_length=1, blank=True, null=True)
    usuarioalta = models.CharField(max_length=20, blank=True, null=True)
    fechaalta = models.DateField(blank=True, null=True)
    usuariomodifica = models.CharField(max_length=20, blank=True, null=True)
    fechamodificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_horas_servicio'
        unique_together = (('servicio', 'fecha_hor_ser', 'hora_ent_ser'), ('servicio', 'fecha_hor_ser', 'hora_ent_ser'),)


class SeProHorasServicioHis(models.Model):
    servicio_id = models.FloatField(primary_key=True)
    fecha_hor_ser = models.DateField()
    hora_ent_ser = models.TimeField()
    hora_sal_ser = models.TimeField(blank=True, null=True)
    estatus_hor_ser = models.CharField(max_length=1, blank=True, null=True)
    total_hor_ser = models.TimeField(blank=True, null=True)
    tipo_hor_ser = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_horas_servicio_his'
        unique_together = (('servicio_id', 'fecha_hor_ser', 'hora_ent_ser'), ('servicio_id', 'fecha_hor_ser', 'hora_ent_ser'),)


class SeProIndAsp(models.Model):
    rowid_pro_ind_asp = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_indicador = models.ForeignKey(SeCatIndicador, models.DO_NOTHING, db_column='rowid_indicador', blank=True, null=True)
    valor_porcentual = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    estatus_indicadores = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_ind_asp'


class SeProPlanEstudio(models.Model):
    rowid_pro_plan_est = models.IntegerField(primary_key=True)
    rowid_asignatura = models.ForeignKey(SeCatAsignatura, models.DO_NOTHING, db_column='rowid_asignatura', blank=True, null=True)
    rowid_plan_est = models.ForeignKey(SeCatPlaEstudio, models.DO_NOTHING, db_column='rowid_plan_est', blank=True, null=True)
    rowid_grado = models.ForeignKey(SeCatGrado, models.DO_NOTHING, db_column='rowid_grado', blank=True, null=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    horas_plan_est = models.IntegerField()
    creditos_plan_est = models.DecimalField(max_digits=5, decimal_places=2)
    nota_minima_apro_est = models.DecimalField(max_digits=5, decimal_places=2)
    valor_pon_final = models.DecimalField(max_digits=5, decimal_places=2)
    estatus_pea = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_plan_estudio'


class SeProProyectoServicio(models.Model):
    rowid_car = models.OneToOneField(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    id_programa = models.ForeignKey('SeTabProgramasServicio', models.DO_NOTHING, db_column='id_programa')
    cantidad_alumnosps = models.IntegerField(blank=True, null=True)
    actividadps = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_proyecto_servicio'
        unique_together = (('rowid_car', 'id_programa'), ('rowid_car', 'id_programa'),)


class SeProRegistroGlobal(models.Model):
    servicio_id = models.FloatField(primary_key=True)
    fecha_reg_global = models.DateField()
    tipo_servicio_glo = models.CharField(max_length=1, blank=True, null=True)
    conteo_real_glo = models.TimeField(blank=True, null=True)
    conteo_modif_glo = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_pro_registro_global'
        unique_together = (('servicio_id', 'fecha_reg_global'), ('servicio_id', 'fecha_reg_global'),)


class SeTabAceptadoHis(models.Model):
    id_indicador_ace_his = models.IntegerField(primary_key=True)
    id_uni_asp_his = models.ForeignKey('SeTabAspiranteHis', models.DO_NOTHING, db_column='id_uni_asp_his', blank=True, null=True)
    id_div_asp_his = models.IntegerField(blank=True, null=True)
    id_car_asp_his = models.IntegerField(blank=True, null=True)
    folio_utn_asp_his = models.CharField(max_length=20, blank=True, null=True)
    calificacion_ace_his = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    folio_cen_ace_his = models.FloatField(blank=True, null=True)
    periodo_ace_his = models.IntegerField(blank=True, null=True)
    anio_ace_his = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_aceptado_his'


class SeTabAceptados(models.Model):
    rowid_indicador = models.ForeignKey(SeCatIndicador, models.DO_NOTHING, db_column='rowid_indicador')
    rowid_car = models.OneToOneField('SeTabAspirante', models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    folio_utn_asp = models.CharField(max_length=20)
    calficacion_ace = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    folio_cen_ace = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_aceptados'
        unique_together = (('rowid_car', 'rowid_indicador', 'folio_utn_asp'), ('rowid_car', 'rowid_indicador', 'folio_utn_asp'),)


class SeTabAsesoresEquipo(models.Model):
    id_matricula = models.OneToOneField('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    rowid_car = models.ForeignKey(SeCatEmpleado, models.DO_NOTHING, db_column='rowid_car')
    rowid_empleado = models.IntegerField()
    rowid_grupo = models.ForeignKey(SeCatGrupo, models.DO_NOTHING, db_column='rowid_grupo')
    nombre_equipo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_asesores_equipo'


class SeTabAspirante(models.Model):
    rowid_car = models.OneToOneField(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    folio_utn_asp = models.CharField(max_length=20)
    rowid_area_bac = models.ForeignKey(SeCatAreaBachillerato, models.DO_NOTHING, db_column='rowid_area_bac', blank=True, null=True)
    rowid_medio_dif = models.ForeignKey(SeCatMedioDifusion, models.DO_NOTHING, db_column='rowid_medio_dif', blank=True, null=True)
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
        unique_together = (('rowid_car', 'folio_utn_asp'), ('rowid_car', 'folio_utn_asp'),)


class SeTabAspiranteHis(models.Model):
    id_uni_asp_his = models.IntegerField(primary_key=True)
    id_div_asp_his = models.IntegerField()
    id_car_asp_his = models.IntegerField()
    folio_utn_asp_his = models.CharField(max_length=20)
    id_tipo_esc_his = models.IntegerField(blank=True, null=True)
    id_medio_dif_his = models.IntegerField(blank=True, null=True)
    id_area_bac_his = models.IntegerField(blank=True, null=True)
    fecha_alt_asp_his = models.DateField(blank=True, null=True)
    mpo_o_alca_nac_asp_his = models.IntegerField(blank=True, null=True)
    ent_fed_nac_asp_his = models.IntegerField(blank=True, null=True)
    calle_asp_his = models.CharField(max_length=60, blank=True, null=True)
    num_int_asp_his = models.IntegerField(blank=True, null=True)
    num_ext_asp_his = models.IntegerField(blank=True, null=True)
    col_asp_his = models.IntegerField(blank=True, null=True)
    codigo_postal_asp_his = models.CharField(max_length=5, blank=True, null=True)
    tel_cas_asp_his = models.CharField(max_length=15, blank=True, null=True)
    telefono_oficina_asp_his = models.CharField(max_length=15, blank=True, null=True)
    mundel_dom_asp_his = models.IntegerField(blank=True, null=True)
    entfed_dom_asp_his = models.IntegerField(blank=True, null=True)
    sexo_asp_his = models.CharField(max_length=1, blank=True, null=True)
    edad_asp_his = models.IntegerField(blank=True, null=True)
    estado_civil_asp_his = models.CharField(max_length=1, blank=True, null=True)
    trabaja_asp_his = models.CharField(max_length=1, blank=True, null=True)
    tipo_de_sangre_asp_his = models.CharField(max_length=10, blank=True, null=True)
    promedio_asp_his = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecini_bach_asp_his = models.IntegerField(blank=True, null=True)
    fecfin_bach_asp_his = models.IntegerField(blank=True, null=True)
    rfc_asp_his = models.CharField(max_length=15, blank=True, null=True)
    curp_asp_his = models.CharField(max_length=25, blank=True, null=True)
    nom_esc_pro_asp_his = models.CharField(max_length=50, blank=True, null=True)
    estatus_asp_his = models.CharField(max_length=1, blank=True, null=True)
    fecha_nac_asp_his = models.DateField(blank=True, null=True)
    materno_asp_his = models.CharField(max_length=30, blank=True, null=True)
    paterno_asp_his = models.CharField(max_length=30, blank=True, null=True)
    folio_cen_asp_his = models.IntegerField(blank=True, null=True)
    nombre_asp_his = models.CharField(max_length=40, blank=True, null=True)
    tipo_publica_privada_asp_his = models.CharField(max_length=1, blank=True, null=True)
    periodo_asp_his = models.IntegerField(blank=True, null=True)
    anio_asp_his = models.IntegerField(blank=True, null=True)
    mat_tutor_asp_his = models.CharField(max_length=30, blank=True, null=True)
    pat_tutor_asp_his = models.CharField(max_length=30, blank=True, null=True)
    nombre_tutor_asp_his = models.CharField(max_length=40, blank=True, null=True)
    generacio_asp_his = models.IntegerField(blank=True, null=True)
    entidad_asp_bach_his = models.IntegerField(blank=True, null=True)
    municipio_asp_bach_his = models.IntegerField(blank=True, null=True)
    ronda_asp_his = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_aspirante_his'
        unique_together = (('id_uni_asp_his', 'id_div_asp_his', 'id_car_asp_his', 'folio_utn_asp_his'), ('id_uni_asp_his', 'id_div_asp_his', 'id_car_asp_his', 'folio_utn_asp_his'),)


class SeTabBitacora(models.Model):
    usuario_bit = models.CharField(primary_key=True, max_length=10)
    fecha_bit = models.DateField()
    consecutivo_bit = models.IntegerField()
    movimiento_bit = models.CharField(max_length=1, blank=True, null=True)
    atributo_ant_bit = models.CharField(max_length=20, blank=True, null=True)
    atributo_nvo_bit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_bitacora'
        unique_together = (('usuario_bit', 'fecha_bit', 'consecutivo_bit'), ('usuario_bit', 'fecha_bit', 'consecutivo_bit'),)


class SeTabCalifFinalEgre(models.Model):
    id_uni = models.IntegerField(primary_key=True)
    id_div = models.IntegerField()
    id_car = models.IntegerField()
    id_matricula_egre = models.CharField(max_length=20)
    id_asignatura_calfin_egre = models.CharField(max_length=20)
    id_plan_calfin_egre = models.IntegerField()
    periodo_calfin_egre = models.IntegerField()
    id_grado_calfin_egre = models.IntegerField()
    anio_calfin_egre = models.IntegerField()
    calficacion_egre = models.DecimalField(max_digits=6, decimal_places=3)
    calificacion_ponderada_egre = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    fecha_alta_calfin_egre = models.DateField(blank=True, null=True)
    user_alta_calfin_egre = models.CharField(max_length=10, blank=True, null=True)
    fecha_baja_calfin_egre = models.DateField(blank=True, null=True)
    user_baja_calfin_egre = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_calfin_egre = models.DateField(blank=True, null=True)
    user_cambio_calfin_egre = models.CharField(max_length=10, blank=True, null=True)
    estatus_calfin_egre = models.CharField(max_length=1, blank=True, null=True)
    comentario_calfin_egre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_calif_final_egre'
        unique_together = (('id_uni', 'id_div', 'id_car', 'id_matricula_egre', 'id_asignatura_calfin_egre', 'id_plan_calfin_egre', 'periodo_calfin_egre', 'id_grado_calfin_egre', 'anio_calfin_egre'), ('id_uni', 'id_div', 'id_car', 'id_matricula_egre', 'id_asignatura_calfin_egre', 'id_plan_calfin_egre', 'periodo_calfin_egre', 'id_grado_calfin_egre', 'anio_calfin_egre'),)


class SeTabCalificacionFinal(models.Model):
    rowid_asignatura = models.OneToOneField(SeCatAsignatura, models.DO_NOTHING, db_column='rowid_asignatura', primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car')
    rowid_grupo = models.ForeignKey(SeCatGrupo, models.DO_NOTHING, db_column='rowid_grupo')
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula')
    id_plan_calfin = models.IntegerField()
    anio_calfin = models.IntegerField()
    parcial_calfin = models.IntegerField()
    periodo_calfin = models.IntegerField()
    calficacion = models.DecimalField(max_digits=6, decimal_places=3)
    calificacion_ponderada = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    fecha_alta_calfin = models.DateField(blank=True, null=True)
    user_alta_calfin = models.CharField(max_length=10, blank=True, null=True)
    fecha_baja_calfin = models.DateField(blank=True, null=True)
    user_baja_calfin = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_calfin = models.DateField(blank=True, null=True)
    user_cambio_calfin = models.CharField(max_length=10, blank=True, null=True)
    estatus_calfin = models.CharField(max_length=1, blank=True, null=True)
    comentario_calfin = models.CharField(max_length=100, blank=True, null=True)
    matri_calfin = models.FloatField(blank=True, null=True)
    id_empleado_calfin = models.IntegerField(blank=True, null=True)
    calificacion_anterior = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    letra_numero = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_calificacion_final'
        unique_together = (('rowid_asignatura', 'rowid_car', 'rowid_grupo', 'id_matricula', 'id_plan_calfin', 'anio_calfin', 'parcial_calfin', 'periodo_calfin'), ('rowid_asignatura', 'rowid_car', 'rowid_grupo', 'id_matricula', 'id_plan_calfin', 'anio_calfin', 'parcial_calfin', 'periodo_calfin'),)


class SeTabCalificacionPar(models.Model):
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula')
    rowid_car = models.OneToOneField(SeCatEmpleado, models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    rowid_empleado = models.IntegerField()
    rowid_pro_asi_ind = models.ForeignKey(SeProAsiIndicador, models.DO_NOTHING, db_column='rowid_pro_asi_ind')
    parcial_cal = models.IntegerField()
    periodo_cal = models.IntegerField()
    id_grupo_par = models.IntegerField()
    anio_cal = models.IntegerField()
    calificacion_par = models.DecimalField(max_digits=6, decimal_places=3)
    fecha_alta_par = models.DateField(blank=True, null=True)
    user_alta_par = models.CharField(max_length=10, blank=True, null=True)
    fecha_baja_par = models.DateField(blank=True, null=True)
    user_baja_par = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_par = models.DateField(blank=True, null=True)
    user_cambio_par = models.CharField(max_length=10, blank=True, null=True)
    comentario_cal_par = models.CharField(max_length=255, blank=True, null=True)
    estatus_calpar = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_calificacion_par'
        unique_together = (('rowid_car', 'id_matricula', 'rowid_empleado', 'rowid_pro_asi_ind', 'parcial_cal', 'periodo_cal', 'id_grupo_par', 'anio_cal'), ('rowid_car', 'id_matricula', 'rowid_empleado', 'rowid_pro_asi_ind', 'parcial_cal', 'periodo_cal', 'id_grupo_par', 'anio_cal'),)


class SeTabCambioCarrera(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    id_uni = models.IntegerField()
    id_div = models.IntegerField()
    id_car = models.IntegerField()
    rowid_tipo_cambio = models.ForeignKey(SeCatTipoCambio, models.DO_NOTHING, db_column='rowid_tipo_cambio', blank=True, null=True)
    id_div_cambio = models.IntegerField(blank=True, null=True)
    id_car_cambio = models.IntegerField(blank=True, null=True)
    anio_cambio = models.IntegerField(blank=True, null=True)
    periodo_cambio = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    fecha_cambio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_cambio_carrera'
        unique_together = (('id_matricula', 'id_uni', 'id_div', 'id_car'), ('id_matricula', 'id_uni', 'id_div', 'id_car'),)


class SeTabCeneval(models.Model):
    folio_cen = models.CharField(primary_key=True, max_length=15)
    identifica_x = models.CharField(max_length=8, blank=True, null=True)
    numver = models.CharField(max_length=2, blank=True, null=True)
    nombre_aspirante = models.CharField(max_length=60, blank=True, null=True)
    esc_proc = models.CharField(max_length=4, blank=True, null=True)
    tipo_reg = models.CharField(max_length=15, blank=True, null=True)
    tipo_pla = models.CharField(max_length=26, blank=True, null=True)
    sistema = models.CharField(max_length=16, blank=True, null=True)
    dur_plan = models.CharField(max_length=9, blank=True, null=True)
    edo_civi = models.CharField(max_length=26, blank=True, null=True)
    edad = models.CharField(max_length=11, blank=True, null=True)
    sexo = models.CharField(max_length=9, blank=True, null=True)
    term_bac = models.CharField(max_length=8, blank=True, null=True)
    term_ext = models.CharField(max_length=11, blank=True, null=True)
    raz_inte = models.CharField(max_length=13, blank=True, null=True)
    mat_repr = models.CharField(max_length=8, blank=True, null=True)
    pro_bach = models.CharField(max_length=12, blank=True, null=True)
    cal_aula = models.CharField(max_length=10, blank=True, null=True)
    cal_lab = models.CharField(max_length=10, blank=True, null=True)
    cal_bibl = models.CharField(max_length=10, blank=True, null=True)
    cal_comp = models.CharField(max_length=10, blank=True, null=True)
    cal_audi = models.CharField(max_length=10, blank=True, null=True)
    cal_espa = models.CharField(max_length=10, blank=True, null=True)
    cal_area = models.CharField(max_length=10, blank=True, null=True)
    cal_cafe = models.CharField(max_length=10, blank=True, null=True)
    cal_cono = models.CharField(max_length=10, blank=True, null=True)
    cal_asis = models.CharField(max_length=10, blank=True, null=True)
    cal_equi = models.CharField(max_length=10, blank=True, null=True)
    cal_aten = models.CharField(max_length=10, blank=True, null=True)
    cal_disc = models.CharField(max_length=10, blank=True, null=True)
    cal_apoy = models.CharField(max_length=10, blank=True, null=True)
    cal_inte = models.CharField(max_length=10, blank=True, null=True)
    cal_acti = models.CharField(max_length=10, blank=True, null=True)
    cal_curs = models.CharField(max_length=10, blank=True, null=True)
    esco_pad = models.CharField(max_length=54, blank=True, null=True)
    esco_mad = models.CharField(max_length=54, blank=True, null=True)
    esco_hea = models.CharField(max_length=54, blank=True, null=True)
    esco_heb = models.CharField(max_length=54, blank=True, null=True)
    esco_hec = models.CharField(max_length=54, blank=True, null=True)
    vive_con = models.CharField(max_length=31, blank=True, null=True)
    prin_eco = models.CharField(max_length=28, blank=True, null=True)
    depe_eco = models.CharField(max_length=8, blank=True, null=True)
    tip_casa = models.CharField(max_length=22, blank=True, null=True)
    cuar_tie = models.CharField(max_length=8, blank=True, null=True)
    num_pers = models.CharField(max_length=8, blank=True, null=True)
    num_foco = models.CharField(max_length=2, blank=True, null=True)
    ser_dren = models.CharField(max_length=7, blank=True, null=True)
    ser_agua = models.CharField(max_length=14, blank=True, null=True)
    ser_alum = models.CharField(max_length=17, blank=True, null=True)
    ser_pavi = models.CharField(max_length=19, blank=True, null=True)
    ser_basu = models.CharField(max_length=31, blank=True, null=True)
    ser_tele = models.CharField(max_length=8, blank=True, null=True)
    ser_cale = models.CharField(max_length=18, blank=True, null=True)
    ser_auto = models.CharField(max_length=27, blank=True, null=True)
    ser_vide = models.CharField(max_length=14, blank=True, null=True)
    ser_cabl = models.CharField(max_length=45, blank=True, null=True)
    ser_pc = models.CharField(max_length=11, blank=True, null=True)
    ser_dicc = models.CharField(max_length=26, blank=True, null=True)
    ser_atla = models.CharField(max_length=13, blank=True, null=True)
    ingr_fam = models.CharField(max_length=18, blank=True, null=True)
    ocu_madr = models.CharField(max_length=64, blank=True, null=True)
    ocu_padr = models.CharField(max_length=64, blank=True, null=True)
    trabaja = models.CharField(max_length=2, blank=True, null=True)
    tipo_tra = models.CharField(max_length=10, blank=True, null=True)
    hrs_trab = models.CharField(max_length=11, blank=True, null=True)
    ingr_men = models.CharField(max_length=18, blank=True, null=True)
    trab_des = models.CharField(max_length=60, blank=True, null=True)
    serv_cul = models.CharField(max_length=38, blank=True, null=True)
    desc_col = models.CharField(max_length=10, blank=True, null=True)
    gpo_carr = models.CharField(max_length=8, blank=True, null=True)
    folioa = models.FloatField(blank=True, null=True)
    raz_vive = models.CharField(max_length=2, blank=True, null=True)
    raz_bara = models.CharField(max_length=2, blank=True, null=True)
    raz_empl = models.CharField(max_length=2, blank=True, null=True)
    raz_trab = models.CharField(max_length=2, blank=True, null=True)
    raz_plan = models.CharField(max_length=2, blank=True, null=True)
    raz_curs = models.CharField(max_length=2, blank=True, null=True)
    raz_estu = models.CharField(max_length=2, blank=True, null=True)
    raz_camp = models.CharField(max_length=2, blank=True, null=True)
    raz_ingr = models.CharField(max_length=2, blank=True, null=True)
    raz_nive = models.CharField(max_length=2, blank=True, null=True)
    raz_term = models.CharField(max_length=2, blank=True, null=True)
    raz_prof = models.CharField(max_length=2, blank=True, null=True)
    raz_comu = models.CharField(max_length=2, blank=True, null=True)
    raz_area = models.CharField(max_length=2, blank=True, null=True)
    raz_inde = models.CharField(max_length=2, blank=True, null=True)
    raz_empr = models.CharField(max_length=2, blank=True, null=True)
    raz_cul = models.CharField(max_length=2, blank=True, null=True)
    raz_paga = models.CharField(max_length=2, blank=True, null=True)
    raz_vida = models.CharField(max_length=2, blank=True, null=True)
    raz_fam = models.CharField(max_length=2, blank=True, null=True)
    raz_gust = models.CharField(max_length=2, blank=True, null=True)
    raz_otra = models.CharField(max_length=2, blank=True, null=True)
    cam_mate = models.CharField(max_length=7, blank=True, null=True)
    cam_biol = models.CharField(max_length=7, blank=True, null=True)
    cam_admo = models.CharField(max_length=7, blank=True, null=True)
    cam_hum = models.CharField(max_length=7, blank=True, null=True)
    cam_soc = models.CharField(max_length=7, blank=True, null=True)
    cam_edu = models.CharField(max_length=7, blank=True, null=True)
    cam_idio = models.CharField(max_length=7, blank=True, null=True)
    cam_info = models.CharField(max_length=7, blank=True, null=True)
    cam_plas = models.CharField(max_length=7, blank=True, null=True)
    cam_esce = models.CharField(max_length=7, blank=True, null=True)
    cam_musi = models.CharField(max_length=7, blank=True, null=True)
    cam_manu = models.CharField(max_length=7, blank=True, null=True)
    cam_dpvo = models.CharField(max_length=7, blank=True, null=True)
    uti_clas = models.CharField(max_length=14, blank=True, null=True)
    uti_lib = models.CharField(max_length=14, blank=True, null=True)
    uti_mono = models.CharField(max_length=14, blank=True, null=True)
    uti_dicc = models.CharField(max_length=14, blank=True, null=True)
    uti_rev = models.CharField(max_length=14, blank=True, null=True)
    uti_vid = models.CharField(max_length=14, blank=True, null=True)
    uti_pc = models.CharField(max_length=14, blank=True, null=True)
    uti_expo = models.CharField(max_length=14, blank=True, null=True)
    uti_bibl = models.CharField(max_length=14, blank=True, null=True)
    uti_ejer = models.CharField(max_length=14, blank=True, null=True)
    uti_trab = models.CharField(max_length=14, blank=True, null=True)
    uti_prof = models.CharField(max_length=14, blank=True, null=True)
    uti_comp = models.CharField(max_length=14, blank=True, null=True)
    uti_fam = models.CharField(max_length=14, blank=True, null=True)
    dom_igle = models.CharField(max_length=18, blank=True, null=True)
    dom_fran = models.CharField(max_length=18, blank=True, null=True)
    dom_clas = models.CharField(max_length=18, blank=True, null=True)
    dom_auto = models.CharField(max_length=18, blank=True, null=True)
    entidad = models.CharField(max_length=2, blank=True, null=True)
    ano_ver = models.CharField(max_length=4, blank=True, null=True)
    fecha_apl = models.DateField(blank=True, null=True)
    numero = models.FloatField(blank=True, null=True)
    global_field = models.FloatField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    percentil = models.FloatField(blank=True, null=True)
    porcne = models.FloatField(blank=True, null=True)
    rv = models.FloatField(blank=True, null=True)
    rn = models.FloatField(blank=True, null=True)
    mc = models.FloatField(blank=True, null=True)
    cn = models.FloatField(blank=True, null=True)
    cs = models.FloatField(blank=True, null=True)
    mat = models.FloatField(blank=True, null=True)
    esp = models.FloatField(blank=True, null=True)
    p_global = models.FloatField(blank=True, null=True)
    p_rv = models.FloatField(blank=True, null=True)
    p_rn = models.FloatField(blank=True, null=True)
    p_mc = models.FloatField(blank=True, null=True)
    p_cn = models.FloatField(blank=True, null=True)
    p_cs = models.FloatField(blank=True, null=True)
    p_mat = models.FloatField(blank=True, null=True)
    p_esp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_ceneval'


class SeTabConsLab(models.Model):
    id_matricula = models.OneToOneField('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    foliocl = models.FloatField(blank=True, null=True)
    fechasolicitudcl = models.DateField(blank=True, null=True)
    estatuscl = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_cons_lab'


class SeTabConsMto(models.Model):
    id_matricula = models.OneToOneField('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    fechasolicitud = models.DateField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    folioconstancia = models.FloatField(blank=True, null=True)
    notarjeton = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_cons_mto'


class SeTabConstanciaLaboratorios(models.Model):
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    foliocl = models.FloatField(blank=True, null=True)
    fechasolicitudcl = models.DateField(blank=True, null=True)
    estatuscl = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_constancia_laboratorios'


class SeTabConstanciaMantenimiento(models.Model):
    id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    fechasolicitud = models.DateField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    folioconstancia = models.FloatField(blank=True, null=True)
    notarjeton = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_constancia_mantenimiento'


class SeTabConstanciasEgresados(models.Model):
    rowid_car = models.OneToOneField('SeTabEgresado', models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    id_matricula_egre = models.CharField(max_length=20)
    fechasolicitud = models.DateField(blank=True, null=True)
    estatussolicitud = models.IntegerField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_constancias_egresados'
        unique_together = (('rowid_car', 'id_matricula_egre'), ('rowid_car', 'id_matricula_egre'),)


class SeTabConstanciasHist(models.Model):
    num_documento = models.FloatField(primary_key=True)
    id_matricula = models.FloatField()
    tipo_documento = models.CharField(max_length=2)
    se_id_matricula = models.ForeignKey('SeTabEstudiante', models.DO_NOTHING, db_column='se__id_matricula', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField()
    estatus_impresion = models.CharField(max_length=2, blank=True, null=True)
    fecha_impresion = models.DateField(blank=True, null=True)
    usuario_imprimio = models.IntegerField(blank=True, null=True)
    no_impresiones = models.IntegerField(blank=True, null=True)
    anio_impresion = models.IntegerField(blank=True, null=True)
    folio_com = models.CharField(max_length=27, blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_constancias_hist'
        unique_together = (('num_documento', 'id_matricula', 'tipo_documento'), ('num_documento', 'id_matricula', 'tipo_documento'),)


class SeTabEgresado(models.Model):
    rowid_car = models.OneToOneField(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    id_matricula_egre = models.CharField(max_length=20)
    nombre_egre = models.CharField(max_length=40)
    paterno_egre = models.CharField(max_length=30)
    materno_egre = models.CharField(max_length=30)
    id_academico_egre = models.IntegerField(blank=True, null=True)
    id_escuela_egre = models.IntegerField(blank=True, null=True)
    id_especialidad_egre = models.IntegerField(blank=True, null=True)
    rfc_egre = models.CharField(max_length=15, blank=True, null=True)
    curp_egre = models.CharField(max_length=25, blank=True, null=True)
    direccion_egre = models.CharField(max_length=60, blank=True, null=True)
    edo_egre = models.IntegerField(blank=True, null=True)
    mpodel_egre = models.IntegerField(blank=True, null=True)
    col_egre = models.IntegerField(blank=True, null=True)
    telefono_egre = models.CharField(max_length=15, blank=True, null=True)
    email_egre = models.CharField(max_length=50, blank=True, null=True)
    sexo_egre = models.CharField(max_length=1)
    fecha_alta_egre = models.DateField()
    user_alta_egre = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_egre = models.DateField(blank=True, null=True)
    user_cambio_egre = models.CharField(max_length=10, blank=True, null=True)
    codpos_egre = models.CharField(max_length=5, blank=True, null=True)
    fec_nac_egre = models.DateField(blank=True, null=True)
    turno_egre = models.IntegerField(blank=True, null=True)
    generacion_egre = models.IntegerField(blank=True, null=True)
    periodo_egre = models.IntegerField(blank=True, null=True)
    anio_egre = models.IntegerField(blank=True, null=True)
    estado_civil_egre = models.CharField(max_length=1, blank=True, null=True)
    trabaja_egre = models.CharField(max_length=1, blank=True, null=True)
    tel_trabajo_egre = models.CharField(max_length=15, blank=True, null=True)
    edad_egre = models.IntegerField(blank=True, null=True)
    salario_egre = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    perfil_profesional_egre = models.CharField(max_length=1, blank=True, null=True)
    empleo_ult_anio_egre = models.CharField(max_length=1, blank=True, null=True)
    incremento_salarial_egre = models.CharField(max_length=1, blank=True, null=True)
    estudio_ref_terminado_egre = models.CharField(max_length=1, blank=True, null=True)
    porcentaje_avance_egre = models.IntegerField(blank=True, null=True)
    busco_empleo_egre = models.CharField(max_length=1, blank=True, null=True)
    comentario_egre = models.CharField(max_length=255, blank=True, null=True)
    estatus_egre = models.CharField(max_length=1, blank=True, null=True)
    estatus_loc_egre = models.CharField(max_length=1, blank=True, null=True)
    edo_nac_egre = models.IntegerField(blank=True, null=True)
    mundel_nac_egre = models.IntegerField(blank=True, null=True)
    estado_egre = models.CharField(max_length=1, blank=True, null=True)
    num_ser_egre = models.FloatField(blank=True, null=True)
    fec_ser_egre = models.DateField(blank=True, null=True)
    tel_rec_egre = models.CharField(max_length=15, blank=True, null=True)
    tel_celular_egre = models.CharField(max_length=15, blank=True, null=True)
    ext_tel_ofi_egre = models.CharField(max_length=6, blank=True, null=True)
    tel_fax_egre = models.CharField(max_length=15, blank=True, null=True)
    num_acta = models.FloatField(blank=True, null=True)
    titulado = models.CharField(max_length=3, blank=True, null=True)
    fec_pres_mem = models.DateField(blank=True, null=True)
    esc_pros = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_egresado'
        unique_together = (('rowid_car', 'id_matricula_egre'), ('rowid_car', 'id_matricula_egre'),)


class SeTabEmpCar(models.Model):
    rowid_emp_car = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatEmpleado, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_empleado = models.IntegerField(blank=True, null=True)
    rowid_institucion = models.ForeignKey(SeCatInstitucion, models.DO_NOTHING, db_column='rowid_institucion', blank=True, null=True)
    descri_corto_car_emp = models.CharField(max_length=10, blank=True, null=True)
    descri_largo_car_emp = models.CharField(max_length=50, blank=True, null=True)
    estatus_inst = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_emp_car'


class SeTabEstServicioHis(models.Model):
    servicio_id = models.FloatField(primary_key=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    id_empleado = models.IntegerField(blank=True, null=True)
    id_programa = models.CharField(max_length=15, blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    id_depto = models.CharField(max_length=3, blank=True, null=True)
    conse_depto = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_ini_ser = models.DateField(blank=True, null=True)
    fecha_fin_ser = models.DateField(blank=True, null=True)
    anio_ser = models.IntegerField(blank=True, null=True)
    periodo_ser = models.IntegerField(blank=True, null=True)
    generacion_ser = models.FloatField(blank=True, null=True)
    estatus_ser = models.CharField(max_length=3, blank=True, null=True)
    tipo_ser = models.CharField(max_length=2, blank=True, null=True)
    turno_ser = models.CharField(max_length=1, blank=True, null=True)
    hora_ent_serint = models.TimeField(blank=True, null=True)
    hora_sal_serint = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_est_servicio_his'


class SeTabEstatusTitulado(models.Model):
    id_matricula_egre = models.CharField(primary_key=True, max_length=20)
    rowid_car = models.ForeignKey(SeTabEgresado, models.DO_NOTHING, db_column='rowid_car')
    se_id_matricula_egre = models.CharField(db_column='se__id_matricula_egre', max_length=20)  # Field renamed because it contained more than one '_' in a row.
    id_estatus_tit = models.ForeignKey(SeCatEstatusTitulado, models.DO_NOTHING, db_column='id_estatus_tit')
    foliodgp = models.FloatField(blank=True, null=True)
    nocedula = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    fec_entrega_titulo = models.DateField(blank=True, null=True)
    fec_entrega_cedula = models.DateField(blank=True, null=True)
    foliotitulo = models.FloatField(blank=True, null=True)
    anio_titulacion = models.IntegerField(blank=True, null=True)
    periodo_titulacion = models.IntegerField(blank=True, null=True)
    fec_alta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_estatus_titulado'


class SeTabEstudiante(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    rowid_becas = models.ForeignKey(SeCatBecas, models.DO_NOTHING, db_column='rowid_becas', blank=True, null=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    rowid_grupo = models.ForeignKey(SeCatGrupo, models.DO_NOTHING, db_column='rowid_grupo', blank=True, null=True)
    nombre_estu = models.CharField(max_length=40)
    paterno_est = models.CharField(max_length=30)
    materno_est = models.CharField(max_length=30)
    rfc_est = models.CharField(max_length=15)
    curp_est = models.CharField(max_length=25)
    direccion_est = models.CharField(max_length=60)
    telefono_est = models.CharField(max_length=15, blank=True, null=True)
    email_est = models.CharField(max_length=50, blank=True, null=True)
    sexo_est = models.CharField(max_length=1)
    fecha_alta_est = models.DateField(blank=True, null=True)
    user_alta_est = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_est = models.DateField(blank=True, null=True)
    user_cambio_est = models.CharField(max_length=10, blank=True, null=True)
    estatus_est = models.CharField(max_length=1, blank=True, null=True)
    codpos = models.CharField(max_length=5)
    fec_nac_est = models.DateField()
    turno_est = models.IntegerField(blank=True, null=True)
    generacion_est = models.IntegerField(blank=True, null=True)
    periodo_est = models.IntegerField(blank=True, null=True)
    anio_est = models.IntegerField(blank=True, null=True)
    estado_civil_est = models.CharField(max_length=1, blank=True, null=True)
    mat_tutor_est = models.CharField(max_length=30, blank=True, null=True)
    pat_tutor_est = models.CharField(max_length=30, blank=True, null=True)
    nombre_tutor_est = models.CharField(max_length=40, blank=True, null=True)
    no_folio_est = models.IntegerField(blank=True, null=True)
    entidad_nac = models.IntegerField(blank=True, null=True)
    mpo_del_nac = models.IntegerField(blank=True, null=True)
    trabaja_est = models.CharField(max_length=1, blank=True, null=True)
    tipo_sangre_est = models.CharField(max_length=10, blank=True, null=True)
    id_tipo_esc_est = models.IntegerField(blank=True, null=True)
    id_area_bach_est = models.IntegerField(blank=True, null=True)
    entidad_bach = models.IntegerField(blank=True, null=True)
    mpo_del_bach = models.IntegerField(blank=True, null=True)
    fecha_ini_bach = models.IntegerField(blank=True, null=True)
    fecha_fin_bach = models.IntegerField(blank=True, null=True)
    promedio_gral_bach = models.DecimalField(max_digits=5, decimal_places=2)
    tel_trabajo = models.CharField(max_length=15, blank=True, null=True)
    edad_est = models.IntegerField(blank=True, null=True)
    fecha_vig_est = models.DateField(blank=True, null=True)
    estatus_inscri_est = models.CharField(max_length=1, blank=True, null=True)
    imss_est = models.CharField(max_length=25, blank=True, null=True)
    clinica_est = models.IntegerField(blank=True, null=True)
    num_servicio = models.FloatField(blank=True, null=True)
    fec_ser_social = models.DateField(blank=True, null=True)
    fecha_repos_est = models.DateField(blank=True, null=True)
    matri_est = models.FloatField(blank=True, null=True)
    beca_pro_est = models.CharField(max_length=1, blank=True, null=True)
    usuario_est = models.CharField(max_length=10, blank=True, null=True)
    password_est = models.CharField(max_length=10, blank=True, null=True)
    estatus_biblio = models.CharField(max_length=1, blank=True, null=True)
    tipo_carrera_est = models.IntegerField(blank=True, null=True)
    otras_uts = models.IntegerField(blank=True, null=True)
    no_cedula_tsu = models.CharField(max_length=30, blank=True, null=True)
    no_referencia = models.CharField(max_length=20, blank=True, null=True)
    grasc = models.CharField(max_length=2, blank=True, null=True)
    institucion_seguro = models.CharField(max_length=25, blank=True, null=True)
    otrainstitucionseguro = models.CharField(max_length=40, blank=True, null=True)
    nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    discapacidad = models.CharField(max_length=5, blank=True, null=True)
    tipodiscapacidad = models.CharField(max_length=40, blank=True, null=True)
    foliocertificado = models.CharField(max_length=40, blank=True, null=True)
    fechaexpedicioncer = models.DateField(blank=True, null=True)
    equivalencia = models.CharField(max_length=5, blank=True, null=True)
    parentescotutor = models.CharField(max_length=40, blank=True, null=True)
    tipoestudiante = models.CharField(max_length=5, blank=True, null=True)
    num_ext = models.CharField(max_length=30, blank=True, null=True)
    num_int = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_estudiante'


class SeTabEstudianteDual(models.Model):
    id_matricula = models.OneToOneField(SeTabEstudiante, models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    anio = models.IntegerField()
    periodo = models.IntegerField()
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    nombre_institucion = models.CharField(max_length=250, blank=True, null=True)
    direccion_institucion = models.CharField(max_length=250, blank=True, null=True)
    responsableduali = models.CharField(max_length=75, blank=True, null=True)
    correo_res_duali = models.CharField(max_length=60, blank=True, null=True)
    telefono_res_dual = models.CharField(max_length=18, blank=True, null=True)
    fecha_ini_convenio = models.DateField(blank=True, null=True)
    fecha_ingreso_dual = models.DateField(blank=True, null=True)
    fecha_egreso_dual = models.DateField(blank=True, null=True)
    fecha_egreso_utn = models.DateField(blank=True, null=True)
    becacomecyt = models.CharField(max_length=4, blank=True, null=True)
    montocomecyt = models.FloatField(blank=True, null=True)
    becaempresa = models.CharField(max_length=4, blank=True, null=True)
    montobecaempresa = models.FloatField(blank=True, null=True)
    estatusdual = models.CharField(max_length=4, blank=True, null=True)
    alumnolaborando = models.CharField(max_length=4, blank=True, null=True)
    nombreempresadual = models.CharField(max_length=250, blank=True, null=True)
    giroempresa = models.CharField(max_length=50, blank=True, null=True)
    nombrecontactoempresa = models.CharField(max_length=75, blank=True, null=True)
    telefonocontactoempresa = models.CharField(max_length=18, blank=True, null=True)
    correocontactoempresa = models.CharField(max_length=60, blank=True, null=True)
    cargocontacto = models.CharField(max_length=50, blank=True, null=True)
    calleempresa = models.CharField(max_length=50, blank=True, null=True)
    numeroextempres = models.CharField(max_length=20, blank=True, null=True)
    numerointempresa = models.CharField(max_length=20, blank=True, null=True)
    codposempresa = models.CharField(max_length=10, blank=True, null=True)
    telefonoempresa = models.CharField(max_length=18, blank=True, null=True)
    correoempresa = models.CharField(max_length=50, blank=True, null=True)
    causabaja = models.CharField(max_length=50, blank=True, null=True)
    soportebaja = models.CharField(max_length=10, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    fechaalta = models.DateField(blank=True, null=True)
    usuarioalta = models.CharField(max_length=15, blank=True, null=True)
    fecha_fin_convenio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_estudiante_dual'
        unique_together = (('id_matricula', 'anio', 'periodo'), ('id_matricula', 'anio', 'periodo'),)


class SeTabEstudianteEsta(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    id_empleado = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    id_area = models.IntegerField(blank=True, null=True)
    id_departamento = models.IntegerField(blank=True, null=True)
    id_trabajador = models.IntegerField(blank=True, null=True)
    id_proyecto = models.IntegerField(blank=True, null=True)
    fecha_ini_esta = models.DateField(blank=True, null=True)
    fecha_fin_esta = models.DateField(blank=True, null=True)
    anio_esta = models.IntegerField(blank=True, null=True)
    periodo_esta = models.IntegerField(blank=True, null=True)
    generacion_esta = models.IntegerField(blank=True, null=True)
    estatus_estancia = models.CharField(max_length=1, blank=True, null=True)
    est_agradecimiento = models.CharField(max_length=150, blank=True, null=True)
    fol_carta_com = models.CharField(max_length=15, blank=True, null=True)
    revisor_ortografia = models.IntegerField(blank=True, null=True)
    revisor_abstrac = models.IntegerField(blank=True, null=True)
    no_control = models.CharField(max_length=10, blank=True, null=True)
    sinodal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_estudiante_esta'


class SeTabEstudianteExt(models.Model):
    id_servicio_ext = models.FloatField(primary_key=True)
    id_edo = models.IntegerField(blank=True, null=True)
    id_mundel = models.IntegerField(blank=True, null=True)
    id_col = models.IntegerField(blank=True, null=True)
    fecha_alta_ext = models.DateField(blank=True, null=True)
    carrera_ext = models.CharField(max_length=50, blank=True, null=True)
    escuela_proce_ext = models.CharField(max_length=255, blank=True, null=True)
    matricula_ext = models.FloatField(blank=True, null=True)
    paterno_ext = models.CharField(max_length=30, blank=True, null=True)
    materno_ext = models.CharField(max_length=30, blank=True, null=True)
    nombre_ext = models.CharField(max_length=40, blank=True, null=True)
    fecnac_ext = models.DateField(blank=True, null=True)
    direccion_ext = models.CharField(max_length=60, blank=True, null=True)
    codpos_ext = models.IntegerField(blank=True, null=True)
    telefono_ext = models.CharField(max_length=15, blank=True, null=True)
    email_ext = models.CharField(max_length=40, blank=True, null=True)
    sexo_ext = models.CharField(max_length=1, blank=True, null=True)
    estatus_ext = models.CharField(max_length=1, blank=True, null=True)
    folio_ext = models.FloatField(blank=True, null=True)
    anio_ext = models.IntegerField(blank=True, null=True)
    periodo_ext = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_estudiante_ext'


class SeTabEstudianteExtHis(models.Model):
    id_servicio_ext = models.FloatField(primary_key=True)
    id_edo = models.IntegerField(blank=True, null=True)
    id_mundel = models.IntegerField(blank=True, null=True)
    id_col = models.IntegerField(blank=True, null=True)
    fecha_alta_ext = models.DateField(blank=True, null=True)
    carrera_ext = models.CharField(max_length=50, blank=True, null=True)
    escuela_proce_ext = models.CharField(max_length=255, blank=True, null=True)
    matricula_ext = models.FloatField(blank=True, null=True)
    paterno_ext = models.CharField(max_length=30, blank=True, null=True)
    materno_ext = models.CharField(max_length=30, blank=True, null=True)
    nombre_ext = models.CharField(max_length=40, blank=True, null=True)
    fecnac_ext = models.DateField(blank=True, null=True)
    direccion_ext = models.CharField(max_length=60, blank=True, null=True)
    codpos_ext = models.IntegerField(blank=True, null=True)
    telefono_ext = models.CharField(max_length=15, blank=True, null=True)
    email_ext = models.CharField(max_length=40, blank=True, null=True)
    sexo_ext = models.CharField(max_length=1, blank=True, null=True)
    estatus_ext = models.CharField(max_length=1, blank=True, null=True)
    folio_ext = models.FloatField(blank=True, null=True)
    anio_ext = models.IntegerField(blank=True, null=True)
    periodo_ext = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_estudiante_ext_his'


class SeTabEstudianteServicio(models.Model):
    servicio_id = models.FloatField(primary_key=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    id_empleado = models.IntegerField(blank=True, null=True)
    id_programa = models.CharField(max_length=15, blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    id_depto = models.CharField(max_length=3, blank=True, null=True)
    conse_depto = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_ini_ser = models.DateField(blank=True, null=True)
    fecha_fin_ser = models.DateField(blank=True, null=True)
    anio_ser = models.IntegerField(blank=True, null=True)
    periodo_ser = models.IntegerField(blank=True, null=True)
    generacion_ser = models.FloatField(blank=True, null=True)
    estatus_ser = models.CharField(max_length=3, blank=True, null=True)
    tipo_ser = models.CharField(max_length=2, blank=True, null=True)
    turno_ser = models.CharField(max_length=1, blank=True, null=True)
    hora_ent_serint = models.TimeField(blank=True, null=True)
    hora_sal_serint = models.TimeField(blank=True, null=True)
    registro_em = models.CharField(max_length=20, blank=True, null=True)
    clasificacion_ser = models.CharField(max_length=15, blank=True, null=True)
    beca_ser = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_estudiante_servicio'


class SeTabFechasHoras(models.Model):
    servicio_id = models.IntegerField(primary_key=True)
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'se_tab_fechas_horas'
        unique_together = (('servicio_id', 'fecha_hora'), ('servicio_id', 'fecha_hora'),)


class SeTabFotosAlumnos(models.Model):
    rowid_fotos = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    folio_utn_asp = models.CharField(max_length=20)
    foto_alumno = models.CharField(max_length=1, blank=True, null=True)
    sel_car1 = models.IntegerField(blank=True, null=True)
    sel_car2 = models.IntegerField(blank=True, null=True)
    sel_car3 = models.IntegerField(blank=True, null=True)
    sel_car4 = models.IntegerField(blank=True, null=True)
    sel_car5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_fotos_alumnos'


class SeTabFotosAlumnosHis(models.Model):
    folio_utn_asp_his = models.CharField(primary_key=True, max_length=20)
    id_car_asp_his = models.IntegerField()
    id_div_asp_his = models.IntegerField()
    id_uni_asp_his = models.IntegerField()
    foto_alumno_foto_his = models.CharField(max_length=1, blank=True, null=True)
    sel_car1_foto_his = models.IntegerField(blank=True, null=True)
    sel_car2_fotos_his = models.IntegerField(blank=True, null=True)
    sel_car3_fotos_his = models.IntegerField(blank=True, null=True)
    sel_car4_fotos_his = models.IntegerField(blank=True, null=True)
    sel_car5_fotos_his = models.IntegerField(blank=True, null=True)
    periodo_fotos_his = models.IntegerField(blank=True, null=True)
    anio_fotos_his = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_fotos_alumnos_his'
        unique_together = (('folio_utn_asp_his', 'id_car_asp_his', 'id_div_asp_his', 'id_uni_asp_his'), ('folio_utn_asp_his', 'id_car_asp_his', 'id_div_asp_his', 'id_uni_asp_his'),)


class SeTabHorarioEsta(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    cve_dia_esta = models.CharField(max_length=2)
    hora_ini_esta = models.TimeField(blank=True, null=True)
    hora_fin_esta = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_horario_esta'
        unique_together = (('id_matricula', 'cve_dia_esta'), ('id_matricula', 'cve_dia_esta'),)


class SeTabImss(models.Model):
    imss_reg_patronal = models.CharField(max_length=10, blank=True, null=True)
    imss_dig_verificador = models.CharField(max_length=1, blank=True, null=True)
    imss_num_seguridad_social = models.CharField(max_length=10, blank=True, null=True)
    imss_dig_verificador_del_nss = models.CharField(max_length=1, blank=True, null=True)
    imss_ape_paterno = models.CharField(max_length=27, blank=True, null=True)
    imss_ape_materno = models.CharField(max_length=27, blank=True, null=True)
    imss_nom_asegurado = models.CharField(max_length=27, blank=True, null=True)
    imss_filler_1 = models.CharField(max_length=7, blank=True, null=True)
    imss_sexo = models.CharField(max_length=1, blank=True, null=True)
    imss_mes_nacimiento = models.CharField(max_length=2, blank=True, null=True)
    id_localidad = models.CharField(max_length=2, blank=True, null=True)
    imss_tipo_de_trabajador = models.CharField(max_length=1, blank=True, null=True)
    imss_filler_2 = models.CharField(max_length=2, blank=True, null=True)
    imss_fecha_mov = models.CharField(max_length=8, blank=True, null=True)
    imss_uni_med_familiar = models.CharField(max_length=3, blank=True, null=True)
    imss_filler_3 = models.CharField(max_length=2, blank=True, null=True)
    imss_tipo_movimiento = models.CharField(max_length=2, blank=True, null=True)
    imss_guia = models.CharField(max_length=5, blank=True, null=True)
    imss_num_cuenta = models.CharField(primary_key=True, max_length=10)
    imss_digito = models.CharField(max_length=1, blank=True, null=True)
    imss_curp = models.CharField(max_length=18, blank=True, null=True)
    imss_iden_formato = models.CharField(max_length=1, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    nom_padre_imss = models.CharField(max_length=300, blank=True, null=True)
    id_loc_padre = models.CharField(max_length=2, blank=True, null=True)
    fec_nac_padre = models.CharField(max_length=10, blank=True, null=True)
    nom_madre_imss = models.CharField(max_length=300, blank=True, null=True)
    id_loc_madre = models.CharField(max_length=2, blank=True, null=True)
    fec_nac_madre = models.CharField(max_length=10, blank=True, null=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    imss_estatus = models.CharField(max_length=2, blank=True, null=True)
    id_matricula = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_imss'


class SeTabImssHis(models.Model):
    imss_reg_patronal = models.CharField(max_length=10, blank=True, null=True)
    imss_dig_verificador = models.CharField(max_length=1, blank=True, null=True)
    imss_num_seguridad_social = models.CharField(max_length=10, blank=True, null=True)
    imss_dig_verificador_del_nss = models.CharField(max_length=1, blank=True, null=True)
    imss_ape_paterno = models.CharField(max_length=27, blank=True, null=True)
    imss_ape_materno = models.CharField(max_length=27, blank=True, null=True)
    imss_nom_asegurado = models.CharField(max_length=27, blank=True, null=True)
    imss_filler_1 = models.CharField(max_length=7, blank=True, null=True)
    imss_sexo = models.CharField(max_length=1, blank=True, null=True)
    imss_mes_nacimiento = models.CharField(max_length=2, blank=True, null=True)
    id_localidad = models.CharField(max_length=2, blank=True, null=True)
    imss_tipo_de_trabajador = models.CharField(max_length=1, blank=True, null=True)
    imss_filler_2 = models.CharField(max_length=2, blank=True, null=True)
    imss_fecha_mov = models.CharField(max_length=8, blank=True, null=True)
    imss_uni_med_familiar = models.CharField(max_length=3, blank=True, null=True)
    imss_filler_3 = models.CharField(max_length=2, blank=True, null=True)
    imss_tipo_movimiento = models.CharField(max_length=2, blank=True, null=True)
    imss_guia = models.CharField(max_length=5, blank=True, null=True)
    imss_num_cuenta = models.CharField(primary_key=True, max_length=10)
    imss_digito = models.CharField(max_length=1, blank=True, null=True)
    imss_curp = models.CharField(max_length=18, blank=True, null=True)
    imss_iden_formato = models.CharField(max_length=1, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    nom_padre_imss = models.CharField(max_length=300, blank=True, null=True)
    id_loc_padre = models.CharField(max_length=2, blank=True, null=True)
    fec_nac_padre = models.CharField(max_length=10, blank=True, null=True)
    nom_madre_imss = models.CharField(max_length=300, blank=True, null=True)
    id_loc_madre = models.CharField(max_length=2, blank=True, null=True)
    fec_nac_madre = models.CharField(max_length=10, blank=True, null=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    imss_estatus = models.CharField(max_length=2, blank=True, null=True)
    id_matricula = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_imss_his'


class SeTabInformesServico(models.Model):
    id_matricula = models.OneToOneField('SeTabServicioIng', models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    no_informess = models.IntegerField()
    fecha_altass = models.DateField(blank=True, null=True)
    actividades = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_informes_servico'
        unique_together = (('id_matricula', 'no_informess'), ('id_matricula', 'no_informess'),)


class SeTabMovAspiranteHis(models.Model):
    folio_utn_asp_his = models.CharField(primary_key=True, max_length=20)
    id_car_asp_his = models.IntegerField()
    id_div_asp_his = models.IntegerField()
    id_uni_asp_his = models.IntegerField()
    fec_mov_asp = models.DateField()
    anio_mov_asp = models.IntegerField(blank=True, null=True)
    generacion_mov_asp = models.IntegerField(blank=True, null=True)
    peri_mov_asp = models.IntegerField(blank=True, null=True)
    user_mov_asp = models.CharField(max_length=10, blank=True, null=True)
    comen_mov_asp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_mov_aspirante_his'
        unique_together = (('folio_utn_asp_his', 'id_car_asp_his', 'id_div_asp_his', 'id_uni_asp_his', 'fec_mov_asp'), ('folio_utn_asp_his', 'id_car_asp_his', 'id_div_asp_his', 'id_uni_asp_his', 'fec_mov_asp'),)


class SeTabMovEstudiante(models.Model):
    id_matricula = models.OneToOneField(SeTabEstudiante, models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    consecutivo_est = models.IntegerField()
    id_evento_est = models.CharField(max_length=3)
    fecha_mov = models.DateField()
    rowid_tipo_baj = models.ForeignKey(SeCatTipoBajas, models.DO_NOTHING, db_column='rowid_tipo_baj', blank=True, null=True)
    fecha_reingreso_baj = models.DateField(blank=True, null=True)
    id_uni_mov = models.IntegerField(blank=True, null=True)
    id_div_mov = models.IntegerField()
    id_car_mov = models.IntegerField()
    id_gra_mov = models.IntegerField()
    comentario_mov = models.CharField(max_length=400, blank=True, null=True)
    estatus_mov = models.CharField(max_length=1, blank=True, null=True)
    usuario_mov = models.CharField(max_length=10, blank=True, null=True)
    id_grupo_mov = models.IntegerField(blank=True, null=True)
    periodo_baj = models.IntegerField(blank=True, null=True)
    id_asignatura_mov = models.CharField(max_length=20, blank=True, null=True)
    id_empleado_mov = models.IntegerField(blank=True, null=True)
    parcial_mov = models.IntegerField(blank=True, null=True)
    cal_par_mov = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    anio_mov = models.IntegerField(blank=True, null=True)
    cal_par_nva_mov = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    fecha_final_mov = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_mov_estudiante'
        unique_together = (('id_matricula', 'consecutivo_est', 'id_evento_est', 'fecha_mov'), ('id_matricula', 'consecutivo_est', 'id_evento_est', 'fecha_mov'),)


class SeTabMovEstudianteRecu(models.Model):
    id_matricula = models.OneToOneField(SeTabEstudiante, models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    consecutivo_est = models.IntegerField()
    id_evento_est = models.CharField(max_length=3)
    fecha_mov = models.DateField()
    id_tipo_baj = models.IntegerField(blank=True, null=True)
    fecha_reingreso_baj = models.DateField(blank=True, null=True)
    id_uni_mov = models.IntegerField(blank=True, null=True)
    id_div_mov = models.IntegerField()
    id_car_mov = models.IntegerField()
    id_gra_mov = models.IntegerField()
    comentario_mov = models.CharField(max_length=400, blank=True, null=True)
    estatus_mov = models.CharField(max_length=1, blank=True, null=True)
    usuario_mov = models.CharField(max_length=10, blank=True, null=True)
    id_grupo_mov = models.IntegerField(blank=True, null=True)
    periodo_baj = models.IntegerField(blank=True, null=True)
    id_asignatura_mov = models.CharField(max_length=20, blank=True, null=True)
    id_empleado_mov = models.IntegerField(blank=True, null=True)
    parcial_mov = models.IntegerField(blank=True, null=True)
    cal_par_mov = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    anio_mov = models.IntegerField(blank=True, null=True)
    cal_par_nva_mov = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    fecha_final_mov = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_mov_estudiante_recu'
        unique_together = (('id_matricula', 'consecutivo_est', 'id_evento_est', 'fecha_mov'), ('id_matricula', 'consecutivo_est', 'id_evento_est', 'fecha_mov'),)


class SeTabPlaticaServicio(models.Model):
    id_matricula = models.OneToOneField(SeTabEstudiante, models.DO_NOTHING, db_column='id_matricula', primary_key=True)
    anio_platica = models.IntegerField()
    periodo_platica = models.IntegerField()
    fecha_alta = models.DateField(blank=True, null=True)
    folio = models.CharField(max_length=20, blank=True, null=True)
    noconsecutivo = models.IntegerField(blank=True, null=True)
    impresion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_platica_servicio'
        unique_together = (('id_matricula', 'anio_platica', 'periodo_platica'), ('id_matricula', 'anio_platica', 'periodo_platica'),)


class SeTabProgSer(models.Model):
    id_programa = models.CharField(primary_key=True, max_length=15)
    nombre_pgm = models.CharField(max_length=255, blank=True, null=True)
    descri_corta_pgm = models.CharField(max_length=10, blank=True, null=True)
    comentario_pgm = models.CharField(max_length=20, blank=True, null=True)
    estatus_pgm = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_prog_ser'


class SeTabProgramasServicio(models.Model):
    id_programa = models.IntegerField(primary_key=True)
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car')
    se_rowid_car = models.ForeignKey(SeCatEmpleado, models.DO_NOTHING, db_column='se__rowid_car')  # Field renamed because it contained more than one '_' in a row.
    rowid_empleado = models.IntegerField()
    nombre_proyectopss = models.CharField(max_length=100, blank=True, null=True)
    dias_laborarpss = models.CharField(max_length=30, blank=True, null=True)
    hora_entpss = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hora_salps = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    objetivo_proyectopss = models.CharField(max_length=250, blank=True, null=True)
    impacto_proyectopss = models.CharField(max_length=100, blank=True, null=True)
    metas_proyectopss = models.CharField(max_length=100, blank=True, null=True)
    beneficiariospss = models.CharField(max_length=100, blank=True, null=True)
    estatus_pss = models.CharField(max_length=4, blank=True, null=True)
    clave_internapss = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_programas_servicio'


class SeTabRegistroTitulos(models.Model):
    id_matricula_tit = models.FloatField(primary_key=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField()
    estatus_impresion = models.CharField(max_length=2, blank=True, null=True)
    fecha_impresion = models.DateField(blank=True, null=True)
    usuario_imprimio = models.IntegerField(blank=True, null=True)
    no_impresiones = models.IntegerField(blank=True, null=True)
    anio_impresion = models.IntegerField(blank=True, null=True)
    folio_tit = models.CharField(max_length=8, blank=True, null=True)
    libro_tit = models.IntegerField(blank=True, null=True)
    foja_tit = models.IntegerField(blank=True, null=True)
    num_documento = models.FloatField()

    class Meta:
        managed = False
        db_table = 'se_tab_registro_titulos'
        unique_together = (('id_matricula_tit', 'num_documento'), ('id_matricula_tit', 'num_documento'),)


class SeTabRepActivSs(models.Model):
    servicio_id = models.FloatField(primary_key=True)
    fecha_entrega_act = models.DateField()
    num_reporte = models.IntegerField(blank=True, null=True)
    entrego_rep_act = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_rep_activ_ss'
        unique_together = (('servicio_id', 'fecha_entrega_act'), ('servicio_id', 'fecha_entrega_act'),)


class SeTabServicioIng(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    no_servicioi = models.IntegerField(blank=True, null=True)
    tipo_seri = models.CharField(max_length=10, blank=True, null=True)
    fecha_altai = models.DateField(blank=True, null=True)
    clave_estatali = models.CharField(max_length=40, blank=True, null=True)
    niveli = models.CharField(max_length=40, blank=True, null=True)
    responsablesutn = models.CharField(max_length=150, blank=True, null=True)
    emailssutn = models.CharField(max_length=80, blank=True, null=True)
    nombre_programai = models.CharField(max_length=200, blank=True, null=True)
    responsablei = models.CharField(max_length=150, blank=True, null=True)
    promedioi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_inii = models.DateField(blank=True, null=True)
    fecha_fini = models.DateField(blank=True, null=True)
    carta_presentacioni = models.CharField(max_length=6, blank=True, null=True)
    carta_terminoi = models.CharField(max_length=6, blank=True, null=True)
    carta_acreditacioni = models.CharField(max_length=6, blank=True, null=True)
    horarioi = models.CharField(max_length=75, blank=True, null=True)
    horas_cubiertasi = models.IntegerField(blank=True, null=True)
    por_planestudioi = models.IntegerField(blank=True, null=True)
    becai = models.CharField(max_length=5, blank=True, null=True)
    monto_beca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_servicio = models.IntegerField(blank=True, null=True)
    id_uni = models.IntegerField(blank=True, null=True)
    estatus_seri = models.CharField(max_length=6, blank=True, null=True)
    tipo2 = models.CharField(max_length=6, blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    id_empresa = models.IntegerField(blank=True, null=True)
    cargores = models.CharField(max_length=300, blank=True, null=True)
    emailres = models.CharField(max_length=60, blank=True, null=True)
    telefonores = models.CharField(max_length=20, blank=True, null=True)
    areasig = models.CharField(max_length=150, blank=True, null=True)
    asesorutn = models.CharField(max_length=150, blank=True, null=True)
    cargoautn = models.CharField(max_length=300, blank=True, null=True)
    emailautn = models.CharField(max_length=150, blank=True, null=True)
    telautn = models.CharField(max_length=20, blank=True, null=True)
    tiporegistro = models.CharField(max_length=4, blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    no_cartatermino = models.CharField(max_length=12, blank=True, null=True)
    anio_ser = models.IntegerField(blank=True, null=True)
    horaent = models.CharField(max_length=6, blank=True, null=True)
    horsal = models.CharField(max_length=6, blank=True, null=True)
    actividadesprestador = models.CharField(max_length=400, blank=True, null=True)
    observacion_ser = models.CharField(max_length=300, blank=True, null=True)
    preacreditacion = models.CharField(max_length=12, blank=True, null=True)
    carta_preliberacion = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_servicio_ing'


class SeTabTitulado(models.Model):
    id_uni = models.IntegerField(primary_key=True)
    id_div = models.IntegerField()
    id_car = models.IntegerField()
    id_matricula_tit = models.CharField(max_length=20)
    rowid_col = models.ForeignKey(SeCatColonia, models.DO_NOTHING, db_column='rowid_col', blank=True, null=True)
    nombre_tit = models.CharField(max_length=40)
    paterno_tit = models.CharField(max_length=30)
    materno_tit = models.CharField(max_length=30)
    rfc_tit = models.CharField(max_length=15, blank=True, null=True)
    curp_tit = models.CharField(max_length=25, blank=True, null=True)
    direccion_tit = models.CharField(max_length=60, blank=True, null=True)
    telefono_tit = models.CharField(max_length=15, blank=True, null=True)
    email_tit = models.CharField(max_length=50, blank=True, null=True)
    sexo_tit = models.CharField(max_length=1, blank=True, null=True)
    fecha_alta_tit = models.DateField(blank=True, null=True)
    user_alta_tit = models.CharField(max_length=10, blank=True, null=True)
    fecha_cambio_tit = models.DateField(blank=True, null=True)
    user_cambio_tit = models.CharField(max_length=10, blank=True, null=True)
    codpos_tit = models.CharField(max_length=5, blank=True, null=True)
    fec_nac_tit = models.DateField(blank=True, null=True)
    turno_tit = models.IntegerField(blank=True, null=True)
    generacion_tit = models.IntegerField(blank=True, null=True)
    periodo_tit = models.IntegerField(blank=True, null=True)
    estado_civil_tit = models.CharField(max_length=1, blank=True, null=True)
    trabaja_tit = models.CharField(max_length=1, blank=True, null=True)
    tel_trabajo_tit = models.CharField(max_length=15, blank=True, null=True)
    edad_tit = models.IntegerField(blank=True, null=True)
    salario_tit = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    perfil_profesional_tit = models.CharField(max_length=1, blank=True, null=True)
    empleo_ult_anio_tit = models.CharField(max_length=1, blank=True, null=True)
    incremento_salarial_tit = models.CharField(max_length=1, blank=True, null=True)
    comentario_tit = models.CharField(max_length=255, blank=True, null=True)
    estatus_tit = models.CharField(max_length=1, blank=True, null=True)
    edo_nac_tit = models.IntegerField(blank=True, null=True)
    mundel_nac_tit = models.IntegerField(blank=True, null=True)
    tel_celular_tit = models.CharField(max_length=15, blank=True, null=True)
    ext_tel_ofi_tit = models.CharField(max_length=6, blank=True, null=True)
    tel_fax_tit = models.CharField(max_length=15, blank=True, null=True)
    num_acta = models.FloatField(blank=True, null=True)
    fec_pres_mem = models.DateField(blank=True, null=True)
    anio_tit = models.IntegerField(blank=True, null=True)
    escuelaprocedencia = models.CharField(max_length=500, blank=True, null=True)
    idedobach = models.CharField(max_length=2, blank=True, null=True)
    idantecedente = models.CharField(max_length=2, blank=True, null=True)
    tipoantecedente = models.CharField(max_length=40, blank=True, null=True)
    fechainiciobach = models.DateField(blank=True, null=True)
    fechafinbach = models.DateField(blank=True, null=True)
    foliocontrol = models.CharField(max_length=12, blank=True, null=True)
    fechainiciocar = models.DateField(blank=True, null=True)
    fechaterminacioncar = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_titulado'
        unique_together = (('id_uni', 'id_div', 'id_car', 'id_matricula_tit'), ('id_uni', 'id_div', 'id_car', 'id_matricula_tit'),)


class SeTabTransferencia(models.Model):
    id_tipo_pag = models.IntegerField(primary_key=True)
    matricula_trans = models.CharField(max_length=20)
    fecha_pago_trans = models.DateField()
    mes_trans = models.IntegerField()
    anio_trans = models.IntegerField()
    consecutivo_trans = models.IntegerField()
    banco_id = models.IntegerField(blank=True, null=True)
    id_cuenta = models.CharField(max_length=30, blank=True, null=True)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    id_grado = models.IntegerField(blank=True, null=True)
    id_grupo = models.IntegerField(blank=True, null=True)
    recibo_trans = models.CharField(max_length=20, blank=True, null=True)
    tipo_estudiante_trans = models.CharField(max_length=3, blank=True, null=True)
    importe_trans = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_deposito_trans = models.DateField(blank=True, null=True)
    nombre_est_trans = models.CharField(max_length=60, blank=True, null=True)
    descripcion_pago = models.CharField(max_length=60, blank=True, null=True)
    estatus_impresion = models.CharField(max_length=1, blank=True, null=True)
    estatus_banco = models.CharField(max_length=1, blank=True, null=True)
    usuario_alta = models.CharField(max_length=10, blank=True, null=True)
    fecha_alta = models.DateField(blank=True, null=True)
    referencia_banco = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_transferencia'
        unique_together = (('id_tipo_pag', 'matricula_trans', 'fecha_pago_trans', 'mes_trans', 'anio_trans', 'consecutivo_trans'), ('id_tipo_pag', 'matricula_trans', 'fecha_pago_trans', 'mes_trans', 'anio_trans', 'consecutivo_trans'),)


class SeTabTutorias(models.Model):
    id_alumno_tutoria = models.FloatField(primary_key=True)
    id_grado_tutoria = models.IntegerField()
    id_empleado_tutoria = models.IntegerField(blank=True, null=True)
    observaciones_tutoria = models.CharField(max_length=1, blank=True, null=True)
    status_tutoria = models.CharField(max_length=1, blank=True, null=True)
    anio_tuto = models.IntegerField(blank=True, null=True)
    periodo_tuto = models.IntegerField(blank=True, null=True)
    cartaconsejo = models.CharField(max_length=5, blank=True, null=True)
    cartahonor = models.CharField(max_length=5, blank=True, null=True)
    apoyopsicologico = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_tutorias'
        unique_together = (('id_alumno_tutoria', 'id_grado_tutoria'), ('id_alumno_tutoria', 'id_grado_tutoria'),)


class SeTabValidaPar(models.Model):
    id_uni = models.IntegerField(primary_key=True)
    id_div = models.IntegerField()
    id_asignatura = models.CharField(max_length=20)
    id_plan_est = models.IntegerField()
    id_grado = models.IntegerField()
    id_car = models.IntegerField()
    parcial_val = models.IntegerField()
    identi_val = models.CharField(max_length=3)
    fec_ini_val = models.DateField(blank=True, null=True)
    fec_fin_val = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tab_valida_par'
        unique_together = (('id_uni', 'id_div', 'id_asignatura', 'id_plan_est', 'id_grado', 'id_car', 'parcial_val', 'identi_val'), ('id_uni', 'id_div', 'id_asignatura', 'id_plan_est', 'id_grado', 'id_car', 'parcial_val', 'identi_val'),)


class SeTemContratosEmp(models.Model):
    id_clave = models.IntegerField(primary_key=True)
    horarios = models.CharField(max_length=200, blank=True, null=True)
    asignaturas = models.CharField(max_length=200, blank=True, null=True)
    grupos = models.CharField(max_length=50, blank=True, null=True)
    pa_sueldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tem_contratos_emp'


class SeTemCredencial(models.Model):
    no_cta = models.CharField(primary_key=True, max_length=15)
    cve_carr = models.CharField(max_length=8, blank=True, null=True)
    no_operador = models.IntegerField(blank=True, null=True)
    cve_area = models.CharField(max_length=8, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    ap_paterno = models.CharField(max_length=255, blank=True, null=True)
    ap_materno = models.CharField(max_length=255, blank=True, null=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    colonia = models.CharField(max_length=255, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    delega = models.CharField(max_length=255, blank=True, null=True)
    edo = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    e_mail = models.CharField(max_length=255, blank=True, null=True)
    fecha_rec_pen = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=5, blank=True, null=True)
    coment_baja = models.CharField(max_length=255, blank=True, null=True)
    fecha_limite = models.DateField(blank=True, null=True)
    ti_usua = models.IntegerField(blank=True, null=True)
    resellos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_tem_credencial'


class Serviciomedico(models.Model):
    nss = models.CharField(primary_key=True, max_length=15)
    curp = models.CharField(max_length=20, blank=True, null=True)
    ap = models.CharField(max_length=75, blank=True, null=True)
    am = models.CharField(max_length=75, blank=True, null=True)
    nom = models.CharField(max_length=75, blank=True, null=True)
    sexo = models.CharField(max_length=2, blank=True, null=True)
    fechaini = models.DateField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    tipomovfin = models.IntegerField(blank=True, null=True)
    baja = models.CharField(max_length=5, blank=True, null=True)
    matricula = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serviciomedico'


class SlTabInventarioLab(models.Model):
    id_mat_lab = models.FloatField(primary_key=True)
    id_etiqueta = models.CharField(max_length=15)
    cant_mat = models.IntegerField(blank=True, null=True)
    estatus_acervo_mat = models.CharField(max_length=1, blank=True, null=True)
    estatus_prestamo = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_tab_inventario_lab'
        unique_together = (('id_mat_lab', 'id_etiqueta'), ('id_mat_lab', 'id_etiqueta'),)


class SlTabMovEstMatLab(models.Model):
    id_matricula = models.FloatField(primary_key=True)
    id_mat_lab = models.FloatField()
    fecha_inicio_deuda = models.DateField(blank=True, null=True)
    cant_deuda = models.IntegerField(blank=True, null=True)
    estatus_mov_deuda = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sl_tab_mov_est_mat_lab'
        unique_together = (('id_matricula', 'id_mat_lab'), ('id_matricula', 'id_mat_lab'),)


class SmTabClinicasImss(models.Model):
    del_field = models.IntegerField(db_column='del', primary_key=True)  # Field renamed because it was a Python reserved word.
    sub = models.CharField(max_length=2)
    umf = models.CharField(max_length=3)
    colonia = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'sm_tab_clinicas_imss'
        unique_together = (('del_field', 'sub', 'umf', 'colonia', 'cp'), ('del_field', 'sub', 'umf', 'colonia', 'cp'),)


class SmTabFoliosImss(models.Model):
    num_seguridad_social = models.CharField(primary_key=True, max_length=10)
    dig_verificador_nss = models.CharField(max_length=1, blank=True, null=True)
    estatus = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_tab_folios_imss'


class SmTabLocalidades(models.Model):
    id_localidad = models.CharField(primary_key=True, max_length=2)
    descri_localidad = models.CharField(max_length=50, blank=True, null=True)
    estatus_loc = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_tab_localidades'


class SmTabPreguntasImss(models.Model):
    id_pregunta_imss = models.IntegerField(primary_key=True)
    descri_larga_preg_imss = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_tab_preguntas_imss'


class SmTabRespuestasImss(models.Model):
    id_respuesta_imss = models.IntegerField(primary_key=True)
    id_pregunta_imss = models.IntegerField()
    descri_larga_respuesta_imss = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_tab_respuestas_imss'
        unique_together = (('id_respuesta_imss', 'id_pregunta_imss'), ('id_respuesta_imss', 'id_pregunta_imss'),)


class Solicitudservicio(models.Model):
    id_servicio_ext = models.FloatField(primary_key=True)
    id_edo = models.IntegerField(blank=True, null=True)
    id_mundel = models.IntegerField(blank=True, null=True)
    id_col = models.IntegerField(blank=True, null=True)
    fecha_alta_ext = models.DateField(blank=True, null=True)
    carrera_ext = models.CharField(max_length=50, blank=True, null=True)
    escuela_proce_ext = models.CharField(max_length=255, blank=True, null=True)
    matricula_ext = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    paterno_ext = models.CharField(max_length=30, blank=True, null=True)
    materno_ext = models.CharField(max_length=30, blank=True, null=True)
    nombre_ext = models.CharField(max_length=40, blank=True, null=True)
    fecnac_ext = models.DateField(blank=True, null=True)
    direccion_ext = models.CharField(max_length=60, blank=True, null=True)
    codpos_ext = models.IntegerField(blank=True, null=True)
    telefono_ext = models.CharField(max_length=15, blank=True, null=True)
    email_ext = models.CharField(max_length=40, blank=True, null=True)
    sexo_ext = models.CharField(max_length=1, blank=True, null=True)
    estatus_ext = models.CharField(max_length=1, blank=True, null=True)
    folio_ext = models.FloatField(blank=True, null=True)
    anio_ext = models.IntegerField()
    periodo_ext = models.IntegerField(blank=True, null=True)
    entidad_nac = models.IntegerField(blank=True, null=True)
    mundel_nac = models.IntegerField(blank=True, null=True)
    semestre_actual = models.IntegerField(blank=True, null=True)
    porcentaje_credito_cub = models.IntegerField(blank=True, null=True)
    otros_estudios = models.CharField(max_length=150, blank=True, null=True)
    institucionexperiencia = models.CharField(max_length=150, blank=True, null=True)
    puestoexperiencia = models.CharField(max_length=50, blank=True, null=True)
    periodoexperiencia = models.CharField(max_length=25, blank=True, null=True)
    areaexperiencia = models.CharField(max_length=50, blank=True, null=True)
    actividadesexperiencia = models.CharField(max_length=150, blank=True, null=True)
    horariodisponible = models.CharField(max_length=50, blank=True, null=True)
    diasdisponible = models.CharField(max_length=50, blank=True, null=True)
    motivoservicio = models.CharField(max_length=250, blank=True, null=True)
    areaservicio = models.CharField(max_length=100, blank=True, null=True)
    actitudes = models.CharField(max_length=250, blank=True, null=True)
    experiencia = models.CharField(max_length=250, blank=True, null=True)
    totalsemestres = models.IntegerField(blank=True, null=True)
    estadocivil = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudservicio'
        unique_together = (('id_servicio_ext', 'anio_ext'), ('id_servicio_ext', 'anio_ext'),)


class SsTabCartaAcreditPres(models.Model):
    num_documento = models.CharField(primary_key=True, max_length=10)
    id_matricula = models.FloatField()
    tipo_documento = models.CharField(max_length=2)
    folio = models.CharField(max_length=30)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    estatus_impresion = models.CharField(max_length=2, blank=True, null=True)
    fecha_impresion = models.DateField(blank=True, null=True)
    usuario_imprimio = models.IntegerField(blank=True, null=True)
    no_impresiones = models.IntegerField(blank=True, null=True)
    anio_impresion = models.IntegerField(blank=True, null=True)
    id_matricula_egre = models.FloatField(blank=True, null=True)
    dirigido = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    importepago = models.FloatField(blank=True, null=True)
    fechapago = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ss_tab_carta_acredit_pres'
        unique_together = (('num_documento', 'id_matricula', 'tipo_documento', 'folio'), ('num_documento', 'id_matricula', 'tipo_documento', 'folio'),)


class SsTabConstancias(models.Model):
    num_documento = models.FloatField(primary_key=True)
    id_matricula = models.FloatField()
    tipo_documento = models.CharField(max_length=2)
    id_uni = models.IntegerField(blank=True, null=True)
    id_div = models.IntegerField(blank=True, null=True)
    id_car = models.IntegerField(blank=True, null=True)
    estatus_impresion = models.CharField(max_length=2, blank=True, null=True)
    fecha_impresion = models.DateField(blank=True, null=True)
    usuario_imprimio = models.IntegerField(blank=True, null=True)
    no_impresiones = models.IntegerField(blank=True, null=True)
    anio_impresion = models.IntegerField(blank=True, null=True)
    id_matricula_egre = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ss_tab_constancias'
        unique_together = (('num_documento', 'id_matricula', 'tipo_documento'), ('num_documento', 'id_matricula', 'tipo_documento'),)


class TablaDeudores(models.Model):
    uni_deu = models.IntegerField(primary_key=True)
    div_deu = models.IntegerField()
    car_deu = models.IntegerField()
    anio_deu = models.IntegerField()
    periodo_deu = models.IntegerField()
    matricula_deu = models.FloatField()
    fecha_ingreso_deu = models.DateField(blank=True, null=True)
    grado_deu = models.IntegerField(blank=True, null=True)
    grupo_deu = models.IntegerField(blank=True, null=True)
    beca_deu = models.IntegerField(blank=True, null=True)
    colegiatura_uno = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    colegiatura_dos = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    colegiatura_tres = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    colegiatura_cuatro = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    reinscripcion_inscripcion = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fecha_ultimo_movimiento = models.DateField(blank=True, null=True)
    saldo_deudor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabla_deudores'
        unique_together = (('uni_deu', 'div_deu', 'car_deu', 'anio_deu', 'periodo_deu', 'matricula_deu'), ('uni_deu', 'div_deu', 'car_deu', 'anio_deu', 'periodo_deu', 'matricula_deu'),)


class TablaPronosticos(models.Model):
    uni_pro = models.IntegerField(primary_key=True)
    div_pro = models.IntegerField()
    anio_pro = models.IntegerField()
    periodo_pro = models.IntegerField()
    fecha_pro = models.DateField()
    tot_alumnos_pro = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_becas_100 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_becas_75 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_becas_50 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bajas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_inscripciones = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_reinscripciones = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    saldo_pro = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabla_pronosticos'
        unique_together = (('uni_pro', 'div_pro', 'anio_pro', 'periodo_pro', 'fecha_pro'), ('uni_pro', 'div_pro', 'anio_pro', 'periodo_pro', 'fecha_pro'),)


class TeCatBancos(models.Model):
    rowid_bancos = models.IntegerField(primary_key=True)
    banco_id = models.IntegerField()
    descri_largo_ban = models.CharField(max_length=50)
    descri_corto_ban = models.CharField(max_length=10)
    estatus_ban = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_cat_bancos'


class TeCatTiposCtas(models.Model):
    rowid_tipo_cta = models.IntegerField(primary_key=True)
    id_tipo_cta = models.IntegerField()
    descri_largo_tipo_cta = models.CharField(max_length=50)
    descri_corto_tipo_cta = models.CharField(max_length=10)
    estatus_tipo_cta = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_cat_tipos_ctas'


class TeProBanDivCuentas(models.Model):
    rowid_ban_ctas = models.IntegerField(primary_key=True)
    banco_id = models.IntegerField()
    id_cuenta = models.CharField(max_length=30)
    id_tipo_cta = models.IntegerField(blank=True, null=True)
    cheque_ini_cta = models.IntegerField(blank=True, null=True)
    cheque_fin_cta = models.IntegerField(blank=True, null=True)
    cheque_act_cta = models.IntegerField(blank=True, null=True)
    estatus_cta = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_pro_ban_div_cuentas'


class TeTabEstDeudores(models.Model):
    rowid_tipo_pag = models.OneToOneField(SeCatTipoPago, models.DO_NOTHING, db_column='rowid_tipo_pag', primary_key=True)
    id_matricula = models.ForeignKey(SeTabEstudiante, models.DO_NOTHING, db_column='id_matricula')
    anio_deudor = models.IntegerField()
    mes_deudor = models.IntegerField()
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    periodo_deudor = models.IntegerField(blank=True, null=True)
    monto_adeudo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    monto_pagado = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    saldo_est = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_tab_est_deudores'
        unique_together = (('rowid_tipo_pag', 'id_matricula', 'anio_deudor', 'mes_deudor'), ('rowid_tipo_pag', 'id_matricula', 'anio_deudor', 'mes_deudor'),)


class TeTabMovimientosCtas(models.Model):
    folio_cheque_mov = models.CharField(primary_key=True, max_length=20)
    banco_id = models.IntegerField(blank=True, null=True)
    id_cuenta = models.CharField(max_length=30, blank=True, null=True)
    tipo_pago_mov = models.CharField(max_length=1, blank=True, null=True)
    ref_factura_mov = models.CharField(max_length=20, blank=True, null=True)
    fec_mov_mov = models.DateField(blank=True, null=True)
    tipo_mov_pres = models.CharField(max_length=1, blank=True, null=True)
    importe_mov = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_tab_movimientos_ctas'


class TeTabPronosAcu(models.Model):
    id_uni_pronos = models.IntegerField(primary_key=True)
    id_div_pronos = models.IntegerField()
    id_car_pronos = models.IntegerField()
    anio_pronos_acu = models.IntegerField()
    per_pronos_acu = models.IntegerField()
    importe_total_acu = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    id_becas_pro_acu = models.IntegerField(blank=True, null=True)
    id_grado_pro_acu = models.IntegerField(blank=True, null=True)
    id_grupo_pro_acu = models.IntegerField(blank=True, null=True)
    descri_pronos_acu = models.CharField(max_length=50, blank=True, null=True)
    tipo_evento_acu = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'te_tab_pronos_acu'
        unique_together = (('id_uni_pronos', 'id_div_pronos', 'id_car_pronos', 'anio_pronos_acu', 'per_pronos_acu', 'tipo_evento_acu'), ('id_uni_pronos', 'id_div_pronos', 'id_car_pronos', 'anio_pronos_acu', 'per_pronos_acu', 'tipo_evento_acu'),)


class TeTabPronosPag(models.Model):
    rowid_tipo_pag = models.OneToOneField(SeCatTipoPago, models.DO_NOTHING, db_column='rowid_tipo_pag', primary_key=True)
    id_matricula = models.ForeignKey(SeTabEstudiante, models.DO_NOTHING, db_column='id_matricula')
    anio_pronos = models.IntegerField()
    mes_pronos = models.IntegerField()
    rowid_car = models.ForeignKey(SeCatCarrera, models.DO_NOTHING, db_column='rowid_car', blank=True, null=True)
    periodo_pronos = models.IntegerField(blank=True, null=True)
    monto_pronos = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    anio_trabajo_pronos = models.IntegerField(blank=True, null=True)
    id_becas_pronos = models.IntegerField(blank=True, null=True)
    id_grado_pronos = models.IntegerField(blank=True, null=True)
    id_grupo_pronos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_tab_pronos_pag'
        unique_together = (('rowid_tipo_pag', 'id_matricula', 'anio_pronos', 'mes_pronos'), ('rowid_tipo_pag', 'id_matricula', 'anio_pronos', 'mes_pronos'),)


class TeTabSaldos(models.Model):
    rowid_ban_ctas = models.OneToOneField(TeProBanDivCuentas, models.DO_NOTHING, db_column='rowid_ban_ctas', primary_key=True)
    id_anio_sal = models.IntegerField()
    id_mes_sal = models.IntegerField()
    saldo_anterior = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    saldo_actual = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'te_tab_saldos'
        unique_together = (('rowid_ban_ctas', 'id_anio_sal', 'id_mes_sal'), ('rowid_ban_ctas', 'id_anio_sal', 'id_mes_sal'),)


class TiProAsigSinodal(models.Model):
    rowid_car = models.OneToOneField(SeCatEmpleado, models.DO_NOTHING, db_column='rowid_car', primary_key=True)
    rowid_empleado = models.IntegerField()
    id_matricula = models.ForeignKey(SeTabEstudianteEsta, models.DO_NOTHING, db_column='id_matricula')
    fecha_presenta = models.DateField()
    hora_presenta = models.DecimalField(max_digits=5, decimal_places=2)
    coment_sinodal = models.CharField(max_length=50, blank=True, null=True)
    estatus_sinodal = models.CharField(max_length=1, blank=True, null=True)
    generacion_sinodal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ti_pro_asig_sinodal'
        unique_together = (('rowid_car', 'rowid_empleado', 'id_matricula'), ('rowid_car', 'rowid_empleado', 'id_matricula'),)


class TiTabTitulados(models.Model):
    id_uni = models.IntegerField(primary_key=True)
    id_div = models.IntegerField()
    id_car = models.IntegerField()
    id_matricula_egre = models.CharField(max_length=20)
    generacion_tit = models.IntegerField(blank=True, null=True)
    periodo_tit = models.IntegerField(blank=True, null=True)
    libro_tit = models.IntegerField(blank=True, null=True)
    foja_tit = models.IntegerField(blank=True, null=True)
    certificado_utn_tit = models.FloatField(blank=True, null=True)
    observaciones_tit = models.CharField(max_length=60, blank=True, null=True)
    estatus_tit = models.CharField(max_length=1, blank=True, null=True)
    fecha_tit = models.DateField(blank=True, null=True)
    estatus_ini_tit = models.CharField(max_length=1, blank=True, null=True)
    num_reg_titulo_tit = models.FloatField(blank=True, null=True)
    num_certif_global_tit = models.CharField(max_length=6, blank=True, null=True)
    num_reg_titulo_prof_tit = models.CharField(max_length=15, blank=True, null=True)
    num_reg_titulo_dir_gral_tit = models.CharField(max_length=15, blank=True, null=True)
    num_cedula_tit = models.FloatField(blank=True, null=True)
    anio_tit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ti_tab_titulados'
        unique_together = (('id_uni', 'id_div', 'id_car', 'id_matricula_egre'), ('id_uni', 'id_div', 'id_car', 'id_matricula_egre'),)
