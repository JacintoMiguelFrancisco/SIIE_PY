import string
from django import forms

#Models
from .models import (
    SeCatPais, SeCatEstado, SeCatMunicipioDelegacion, SeCatAsentamiento,SeCatColonia,  # Direcciones
    SeCatUniversidad, SeCatDivision, SeCatCarrera, SeCatPeriodos, # Universidades
    SeCatPlaEstudio, SeCatAsignatura, SeCatIndicador, SeProPlanEstudio, SeProAsiIndicador, # Plan de Estudio
    SeCatEscuelaProcedencia, SeCatMedioDifusion, SeCatTipoEscuela, SeCatAreaBachillerato, SeProIndAsp, # Aspirantes
    SeTabEstudiante, SeCatDocumentacion,SeCatGrupo,SeCatEstatusEstudiante, SeCatGrado, SeCatSalones, SeCatTipoBajas, SeCatBecas, SeCatTipoCambio, # Estudintes
    SeCatEmpleado, SeCatNivelAcademico, SeCatPlaza, SeCatTipoPuesto, SeCatSueldos, SeCatDeptoEmp, SeCatActividades, SeCatInstitucion, SeTabEmpCar, # Empleados
    SeTabAspirante # Operaciones / Aspirante
)

##########################  Catalogo #################################
# -------------------------------------------- Direcciones --------------------------------------------- #
# Form Paises En este formulario se agrega y tiene habilitado el campo de id
class FormPaises(forms.ModelForm):
    class Meta:
        model = SeCatPais
        fields = '__all__'
        exclude = ('estatus_pais','rowid_pais')
        widgets = {
            'id_pais': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese la clave del pais',
                                                        'style' : 'border-color:#21B64A;',
                                                        }),
            'descri_largo_pais': forms.TextInput(attrs={'class': 'form-control', 
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese el nombre del pais',
                                                        'style' : 'border-color:#21B64A;',
                                                        }),
            'descri_corto_pais': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True', 
                                                        'placeholder': 'Por favor, Ingrese la abreviatura del pais',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'id_pais': 'Clave del Pais *',
                'descri_largo_pais': 'Nombre Pais *',
                'descri_corto_pais': 'Abreviatura *',
        }
# Form Estados
class FormEstados(forms.ModelForm):
    class Meta:
        model = SeCatEstado
        fields = '__all__'
        exclude = ('rowid_edo', 'estatus_edo',)
        widgets = {
            'rowid_pais': forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'id_edo': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la clave del Estado.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_largo_edo': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese nombre del Estado.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_corto_edo': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese abreviatura del Estado.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'rowid_pais': 'Pais: *',
                'id_edo': 'Clave Estado: *',
                'descri_largo_edo': 'Estado: *',
                'descri_corto_edo': 'Abreviatura: *',
                'id_entidad_federativa': 'Clave Entidad Federativa:',
                'c_nom_ent': 'Entidad Federativa: ',
            }
# Form Municipios/Delegaciones 
class FormMunicipiosDelegaciones(forms.ModelForm):
    class Meta:
        model = SeCatMunicipioDelegacion
        fields = '__all__'
        exclude = ('rowid_mundel','estatus_mundel')

        widgets = {
            'rowid_edo': forms.Select(attrs={'class': 'form-control',
                                            'required' : 'True',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'id_mundel': forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese clave del Municipio/Delegación',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'descri_largo_mundel': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese nombre del Municipio/Delegación.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_corto_mundel': forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese abreviatura del Municipio/Delegación.',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
        }
        labels = {
            'rowid_edo' : 'Estado *',
            'id_mundel' : 'Id Municipio/Delegación *',
            'descri_largo_mundel' : 'Municipio/Delegación *',
            'descri_corto_mundel' : 'Abreviatura *',
        }
# Form Asentamiento 
class FormAsentamiento(forms.ModelForm):
    class Meta:
        model = SeCatAsentamiento
        fields = '__all__'
        exclude = ('estatus_asentamiento','rowid_asentamiento')
        widgets = {
            'id_asentamiento': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese la clave del Asentamiento',
                                                        'style' : 'border-color:#21B64A;',
                                                        }),
            'descri_largo_asentamiento': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese el nombre del Asentamiento',
                                                        'style' : 'border-color:#21B64A;',
                                                        }),
            'descri_corto_asentamiento': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese la abreviatura del Asentamiento',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'id_asentamiento': 'Clave del Asentamiento *',
                'descri_largo_asentamiento': 'Nombre Asentamiento *',
                'descri_corto_asentamiento': 'Abreviatura *',
        }
# FORM Colonias
class FormColonias(forms.ModelForm):
    class Meta:
        model = SeCatColonia
        fields = '__all__'
        exclude = ('rowid_col', 'estatus_col') 
        widgets = {
            'rowid_mundel': forms.Select(attrs={'class': 'form-control',
                                            'required' : 'True',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'rowid_asentamiento': forms.Select(attrs={'class': 'form-control',
                                            'required' : 'True',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'id_col': forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese la clave la Colonia',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'descri_largo_col': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese nombre de la Colonia.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
            'descrip_corto_col': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese abreviatura de la Colonia.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
            'codposcol': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese codigo postal de la Colonia.',
                                                'style' : 'border-color:#21B64A;'                                                
                                                }),
        }
        labels = {
            'rowid_mundel': 'Municipio *',
            'rowid_asentamiento': 'Asentamiento *',
            'id_col': 'Clave *',
            'descri_largo_col': 'Colonia *',
            'descrip_corto_col': 'Abreviatura *',
            'codposcol': 'Codigo Postal.',
        }

# -------------------------------------------- Universidad --------------------------------------------- #

# Form Universidad
class FormUniversidad(forms.ModelForm):
    class Meta:
        model = SeCatUniversidad
        fields = '__all__'
        exclude = ('rowid_uni', 'estatus_uni')
        widgets = {
            'rowid_col': forms.Select(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'style' : 'border-color:#21B64A;'
                                                }),
            'id_uni': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Por favor, Ingrese el tipo de organizacion',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'nombre_uni': forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Por favor, Ingrese la direccion',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'tipo_org_uni': forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Por favor, Ingrese el RFC',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'direccion_uni': forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True' ,
                                                    'placeholder': 'Por favor, Ingrese el codigo postal',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'rfc_uni': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese el primer telefono',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'codpos_uni': forms.NumberInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Por favor, Ingrese el segundo telefono',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'telefono1_uni': forms.NumberInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Por favor, Ingrese el tercer telefono',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'telefono2_uni': forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Por favor, Ingrese el primer fax',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'telefono3_uni': forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Por favor, Ingrese el segundo fax',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'ext1_uni': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Por favor, Ingrese la tercer extension',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'ext2_uni': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Por favor, Ingrese la tercer extension',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'ext3_uni': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Por favor, Ingrese la tercer extension',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'mail_uni': forms.EmailInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Por favor, Ingrese el email',
                                                 'style' : 'border-color:#21B64A;'
                                                 }),
            'pagina_internet_uni': forms.URLInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Por favor, Ingrese pagina de internet',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'contacto_uni': forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Por favor, Ingrese el contacto',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
        }
        labels = {
                'rowid_col': 'Colonia *',
                'id_uni': 'Id universidad*',
                'nombre_uni': 'Nombre *',
                'tipo_org_uni': 'Tipo de organizacion *',
                'direccion_uni': 'Dirección *',
                'rfc_uni': 'RFC *',
                'codpos_uni': 'Código postal',
                'telefono1_uni': 'Telefono 1 *',
                'telefono2_uni': 'Telefono 2 *',
                'telefono3_uni': 'Telefono 3 *',
                'ext1_uni': 'Extension 1',
                'ext2_uni': 'Extencion 2',
                'ext3_uni': 'Extencion 3',
                'mail_uni': 'Correo electronico *',
                'pagina_internet_uni': 'Página web*',
                'contacto_uni': 'Contacto *',
            }
# fFORMS DIVISIONES 
class FormDivisiones(forms.ModelForm):
    class Meta:
        model = SeCatDivision
        fields = '__all__'
        exclude = ('rowid_div', 'estatus_div')
        widgets = {
            'rowid_uni': forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'id_div': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese clave de la división.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_larga_div': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;',
                                                        'placeholder': 'Ingrese nombre de la división'}),
            'descri_corta_div': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;',
                                                        'placeholder': 'Ingrese abreviatura de la división'}),
            'representante_div': forms.TextInput(attrs={'class': 'form-control',
                                                           'required' : 'True',
                                                            'style' : 'border-color:#21B64A;',
                                                            'placeholder': 'Ingrese nombre del representante'}),
            'telefono_1_div': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;',
                                                        'placeholder': 'Ingrese 1er teléfono'}),
            'telefono_2_div': forms.TextInput(attrs={'class': 'form-control',
                                                        'style' : 'border-color:#21B64A;',
                                                        'placeholder': 'Ingrese 2do teléfono'}),
            'fax1_div': forms.TextInput(attrs={'class': 'form-control',
                                                'style' : 'border-color:#21B64A;',
                                                'placeholder': 'Ingrese 1er fax'}),
            'fax2_div': forms.TextInput(attrs={'class': 'form-control',
                                                'style' : 'border-color:#21B64A;',
                                                'placeholder': 'Ingrese 2do fax'}),
            'extension1_div': forms.TextInput(attrs={'class': 'form-control',
                                                        'style' : 'border-color:#21B64A;',
                                                        'placeholder': 'Ingrese 1er extensión'}),
            'extension2_div': forms.TextInput(attrs={'class': 'form-control',
                                                        'style' : 'border-color:#21B64A;',
                                                        'placeholder': 'Ingrese 2do extensión'}),
            'mail_div': forms.TextInput(attrs={'class': 'form-control',
                                                'style' : 'border-color:#21B64A;',
                                                'placeholder': 'Ingrese Email de la división'}),
        }
        labels = {
                'rowid_uni': 'Universidad *',
                'id_div':'Clave División *',
                'descri_larga_div': 'Nombre Division *',
                'descri_corta_div': 'Abreviatura División *',
                'representante_div': 'Representante División *',
                'telefono_1_div': 'Teléfono 1 *',
                'telefono_2_div': 'Teléfono 2 ',
                'fax1_div': 'Fax 1 ',
                'fax2_div': 'Fax 2 ',
                'extension1_div': 'Extensión 1 ',
                'extension2_div': 'Extensión 2 ',
                'mail_div': 'Email ',
            }
# Form Carreras
class FormCarreras(forms.ModelForm):
    class Meta:
        model = SeCatCarrera
        fields = '__all__'
        exclude = ('estatus_car','rowid_car' )
        widgets = {
            'rowid_div':forms.Select(attrs={'class': 'form-control',
                                                       'required' : 'True','placeholder': 'Seleccione la Division',
                                                       'style': 'border-color:#21B64A;'}),
            'id_car': forms.NumberInput(attrs={'class': 'form-control',
                                                       'required' : 'True','placeholder': 'Por favor, Ingrese el ID de la carrera',
                                                       'style': 'border-color:#21B64A;'}),
            'descri_largo_car': forms.TextInput(attrs={'class': 'form-control', 
                                                       'placeholder': 'Por favor, Ingrese el nombre de la Carrera',
                                                       'style': 'border-color:#21B64A;'}),
            'descri_corto_car': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la Abreviatura',
                                                       'style': 'border-color:#21B64A;'}),
            'ceneval_car': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el Ceneval',
                                                       'style': 'border-color:#21B64A;'}),
            'descri_largo_tit': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese una Descripcion', 
                                                       'style': 'border-color:#21B64A;'}),
        }
        labels = {
                'rowid_div': 'Division',
                'id_car': 'Id Carrera',
                'descri_largo_car': 'Carrera',
                'descri_corto_car': 'Abreviatura',
                'ceneval_car': 'Ceneval',
                'descri_largo_tit': 'Descripcion',
            }
# Form Periodos
class FormPeriodos(forms.ModelForm):
    PERIODOS = (
        (0,'Seleccione el Periodo'),
        (1,'Enero-Abril'),
        (2,'Mayo-Agosto'),
        (3,'Septiembre-Diciembre')
    )
    periodo_per = forms.ChoiceField(label='Periodo:',choices=PERIODOS,widget=forms.Select(attrs={'class': 'form-control','style': 'border-color:#21B64A;'}))
    class Meta:
        model = SeCatPeriodos
        field = '__all__'
        exclude = ('rowid_per','estatus_per')
        widgets = {
            'rowid_car':forms.Select(attrs={'class': 'form-control', 'placeholder':'Seleccione una Carrera','style': 'border-color:#21B64A;'}),
            'evento_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese evento','style': 'border-color:#21B64A;'}),
            'consecutivo_per': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingrese consecutivo','style': 'border-color:#21B64A;'}),
            'fecha_inicial_per': forms.DateInput(attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA','style': 'border-color:#21B64A;'}),
            'fecha_final_per': forms.DateInput(attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA','style': 'border-color:#21B64A;'}),
            'anio_per': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingresa el año','style': 'border-color:#21B64A;'}),
            'descripcion_per': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese descripcion de la plaza','style': 'border-color:#21B64A;'}),
        }
        labels = {
                'rowid_car':'Carrera',
                'evento_per': 'Evento',
                'consecutivo_per': 'Consecutivo',
                'fecha_inicial_per': 'Fecha inicial',
                'fecha_final_per': 'Fecha final',
                'anio_per': 'Año',
                'descripcion_per': 'Descripcion del Periodo',
            }

# -------------------------------------------- Plan de Estudios  --------------------------------------------- #

# Form PLAN DE ESTUDIO 
class FormsPlaE(forms.ModelForm):
    class Meta:
        model= SeCatPlaEstudio
        fields = '__all__'
        exclude = ('rowid_plan_est', 'estatus_plan_est')
        widgets = {
    'id_plan_est' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el nombre del plan',
                                                            'style' : 'border-color:#21B64A;'
                                                            }),
    'decri_larga_plan_est' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el nombre del plan',
                                                            'style' : 'border-color:#21B64A;'
                                                            }),
    'descri_corta_plan_est' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el nombre del plan',
                                                            'style' : 'border-color:#21B64A;'
                                                            }),
    'fec_alta_estpla'  : forms.DateInput(attrs={'class': 'form-control',
                                                        'placeholder': 'DD/MM/AAAA',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
    'user_alta_estpla': forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el nombre del plan',
                                                            'style' : 'border-color:#21B64A;'
                                                            }),
    'fec_baja_estpla' : forms.DateInput(attrs={'class': 'form-control',
                                                        'placeholder': 'DD/MM/AAAA',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
    'user_baja_estpla' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el nombre del plan',
                                                            'style' : 'border-color:#21B64A;'
                                                            }),
        }
        ###cambiar data tiem por la otra madre
        labels ={
                'id_plan_est' : 'Id plan de estudio *',
                'decri_larga_plan_est' : 'Nombre del Plan *',
                'descri_corta_plan_est' : 'Abreviatura *',
                'fec_alta_estpla' : 'Fecha de alta',
                'user_alta_estpla' : 'Usuario Alta',
                'fec_baja_estpla' : 'Fecha de baja',
                'user_baja_estpla' :'Usuario Baja',
        }
# Form ASIGNATURA
class FormsAsignatura(forms.ModelForm):
    class Meta:
        model = SeCatAsignatura
        fields = '__all__'
        exclude = ('rowid_asignatura','estatus_asi',)
        widgets = {
            'rowid_plan_est': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'rowid_car': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'id_asignatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el nombre de la Asignatura', 'style' : 'border-color:#21B64A;'}),
            'descri_larga_asi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el nombre de la Asignatura', 'style' : 'border-color:#21B64A;'}),
            'descri_corto_asi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la abreviatura del Asignatura', 'style' : 'border-color:#21B64A;'}),
        }
        labels = {
                'rowid_plan_est': 'Plan de estudio',
                'rowid_car': 'Carrera',
                'id_asignatura': 'Id asignatura',
                'descri_larga_asi': 'Nombre Asignatura',
                'descri_corto_asi': 'Abreviatura',
            }
#Form INDICADORES 
class FormsIndicador(forms.ModelForm):
    CONTROL = ( ('E', 'Estudiante '), ('A','Aspirante') )
    cve_control_ind = forms.ChoiceField(label='Control *', choices=CONTROL, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    class Meta:
        model= SeCatIndicador
        fields= '__all__'
        exclude = ('rowid_indicador', 'estatus_ind')
        widgets = {
            'id_indicador' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el Id del indicador.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_largo_ind' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre del indicador.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_corto_ind' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre del indicador.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels ={
                'id_indicador' : 'Id Indicador',
                'descri_largo_ind' : 'Nombre Indicador*',
                'descri_corto_ind' : 'Abreviatura *',
        }
#Form Plan de estudio asignatura 
class FormsPeA(forms.ModelForm):
    class Meta:
        model = SeProPlanEstudio
        fields = '__all__'
        exclude = ('rowid_pro_plan_est','estatus_pea',)
        widgets = {
            'rowid_asignatura' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'rowid_plan_est' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'rowid_grado' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'rowid_car' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'horas_plan_est' :  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese las horas', 'style' : 'border-color:#21B64A;'}),
            'creditos_plan_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese los creditos', 'style' : 'border-color:#21B64A;'}), 
            'nota_minima_apro_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la nota minima', 'style' : 'border-color:#21B64A;'}),
            'valor_pon_final' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el valor final', 'style' : 'border-color:#21B64A;'}),
        }
        labels = {
            'rowid_asignatura' : 'Asignatura',
            'rowid_plan_est' : 'Plan de estudio',
            'rowid_grado' : 'Grado',
            'rowid_car' : 'Carrera',
            'horas_plan_est' : 'Numero de horas',
            'creditos_plan_est' : 'Creditos ',
            'nota_minima_apro_est' : 'Nota minima aprobatoria',
            'valor_pon_final' : 'Valor final',
        }
#Plan de estudio asignatura indicador
class FormsPeaI(forms.ModelForm):
    class Meta:
        model = SeProAsiIndicador
        fields = '__all__'
        exclude = ('rowid_pro_asi_ind', 'estatus_peai',)
        widgets = {
            'rowid_pro_plan_est' : forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}),
            'rowid_indicador' : forms.Select(attrs={'class': 'form-control','style' : 'border-color:#21B64A;'}),
            'porcentaje_pro_asi_idi' :  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el porcentaje', 'style' : 'border-color:#21B64A;'}),
            'comen_pro_asi_ind'  :  forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el comentario', 'style' : 'border-color:#21B64A;'}),    
        }
        labels = {
            'rowid_pro_plan_est' : 'Plan de estudio',
            'rowid_indicador' : 'Indicador',
            'porcentaje_pro_asi_idi' : 'Porcentaje',
            'comen_pro_asi_ind' : 'Comentario',
        }

# -------------------------------------------- Aspirantes --------------------------------------------- #

################## Escuela Procedencia ########################
class FormEscProc(forms.ModelForm):
    class Meta:
        model = SeCatEscuelaProcedencia
        fields = '__all__'
        exclude = ('estatus_esc_proc','rowid_esc_proc')
        widgets = {
            'rowid_mundel': forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;',
                                                        }),
            'cct_esc_proc': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese la clave del Centro de Trabajo',
                                                        'style' : 'border-color:#21B64A;',
                                                        }),
            'nombre_esc_proc': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese el nombre de la Escuela de Procedencia',
                                                        'style' : 'border-color:#21B64A;',
                                                        }),
            'control_esc_proc': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese el control de la escuela de procedencia',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'servicio_esc_proc': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Por favor, Ingrese el servicio de la escuela de procedencia',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'rowid_mundel': 'Municipio *',
                'cct_esc_proc': 'Clave del Centro de Trabajo *',
                'nombre_esc_proc': 'Nombre de la Escuela de Procedencia *',
                'control_esc_proc': 'Tipo de Escuela *',
                'servicio_esc_proc': 'Servicio que ofrece la escuela *',
        }
# FORMS MEDIOS DE DIFUSION 
class FormMediosDifusion(forms.ModelForm):
    class Meta:
        model = SeCatMedioDifusion
        fields = '__all__'
        exclude = ('rowid_medio_dif', 'estatus_dif')
        widgets = {
            'id_medio_dif': forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese clave de la división.',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'descri_largo_meddif': forms.TextInput(attrs={'class': 'form-control','required': 'True',
                                                          'placeholder': 'Ingrese nombre del Medio de Difusión.',
                                                          'required' : 'True',
                                                          'style' : 'border-color:#21B64A;'
                                                          }),
            'descri_corto_meddif': forms.TextInput(attrs={'class': 'form-control','required': 'True',
                                                          'placeholder': 'Ingrese abreviatura del Medio de Difusión.',
                                                          'required' : 'True',
                                                          'style' : 'border-color:#21B64A;'
                                                          }),
        }
        labels = {
                'id_medio_dif': 'Clave Medio de Difusión *',
                'descri_largo_meddif': 'Medio de Difusión *',
                'descri_corto_meddif': 'Abreviatura *',
            }
# Forms TIPOS DE ESCUELAS
class FormTiposEscuelas(forms.ModelForm):
    class Meta:
        model = SeCatTipoEscuela
        fields = '__all__'
        exclude = ('rowid_tipo_esc', 'estatus_esc')
        widgets = {
            'rowid_col': forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'id_tipo_esc':  forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese clave del Tipo de Escuela.',
                                                        'style' : 'border-color:#21B64A;'
                                              }),
            'descri_largo_esc': forms.TextInput(attrs={'class': 'form-control','required': 'True',
                                                       'placeholder': 'Ingrese nombre del Tipo de Escuela.',
                                                       'required' : 'True',
                                                       'style' : 'border-color:#21B64A;'
                                                       }),
            'descri_corta_esc': forms.TextInput(attrs={'class': 'form-control','required': 'True',
                                                       'placeholder': 'Ingrese abreviatura del Tipo de Escuela.',
                                                       'required' : 'True',
                                                       'style' : 'border-color:#21B64A;'
                                                       }),
            'institucion': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Ingrese nombre de la Institución.',
                                                  'style' : 'border-color:#21B64A;'
                                                  }),
            'nombre_plantel': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Ingrese nombre del Plantel.',
                                                     'style' : 'border-color:#21B64A;'
                                                     }),
        }
        labels = {
                'rowid_col' : 'Colonia *',
                'id_tipo_esc' : 'Clave Tipo de Escuela *',
                'descri_largo_esc' : 'Nombre Tipo de Escuela *',
                'descri_corta_esc': 'Abreviatura Tipo de Escuela *',
                'institucion': 'Nombre Institución',
                'nombre_plantel': 'Nombre Plantel',
        }
# Forms ÁREA BACHILLERATO
class FormAreaBachi(forms.ModelForm):
    class Meta:
        model = SeCatAreaBachillerato
        fields = '__all__'
        exclude = ('rowid_area_bac', 'estatus_bac')
        widgets = {
            'id_area_bac':  forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese clave del Área Bachillerato.',
                                                        'style' : 'border-color:#21B64A;'
                                              }),
            'descri_larga_bac': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese nombre del Área Bachillerato',
                                                        'style' : 'border-color:#21B64A;',
                                                        'required' : 'True'
                                                        }),
            'descri_corta_bac': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese abreviatura del Área Bachillerato',
                                                        'style' : 'border-color:#21B64A;',
                                                        'required' : 'True'
                                                      }),
        }
        labels = {
                'id_area_bac' : 'Clave Área Bachillerato *',
                'descri_larga_bac' : 'Nombre Área Bachillerato *',
                'descri_corta_bac' : 'Abreviatura Área Bachillerato *',
            }
# Forms INDICADORES ASPIRANTES
class FormIndAsp(forms.ModelForm):
    class Meta:
        model= SeProIndAsp
        fields= '__all__'
        exclude = ('rowid_pro_ind_asp', 'estatus_indicadores')
        widgets = {
            'rowid_car': forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'rowid_indicador': forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'valor_porcentual': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required': 'True',
                                                        'placeholder': 'Ingrese valor porcentual del Indicador Aspirante.',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                    }),
        }
        labels = {
                'rowid_car' : 'Carrera *',
                'rowid_indicador' : 'Indicador *',
                'valor_porcentual' : 'Valor porcentual del Indicador Aspirante *',
        }

# -------------------------------------------- Estudiantes --------------------------------------------- #

##forms ESTUDANTE
class FormsEstudiante(forms.ModelForm):
    EDOCIVIL = ( ('S', 'Soltero'), ('C','Casado'), ('V','Viudo'), ('D','Divorciado') )
    TRAB = ( ('S', 'Si'), ('N','No') )
    RESSN = ( ('1', 'Si'), ('2','No') )
    TIPEST = ( ('R', 'Regular'), ('I','Irregular') )
    SEXO = ( ('M', 'Masculino'), ('F', 'Femenino') )
    TURN = ( ('1', 'Matutino'), ('2', 'Vespertino') )
    ALBA = ( ('A', 'Alta'), ('B','Baja') )
    TIPESC = ( (1, 'Pública'), (2,'Privada') )
    CONTROL = ( ('E', 'Estudiante '), ('A','Aspirante') )    
    PERIODOS = (
        (0,'Seleccione el Periodo'),
        (1,'Enero-Abril'),
        (2,'Mayo-Agosto'),
        (3,'Septiembre-Diciembre')
    ) 
    discapacidad = forms.ChoiceField(label='Discapacidad *', choices=TRAB, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    tipoestudiante = forms.ChoiceField(label='Tipo Estudiante *', choices=TIPEST, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    grasc = forms.ChoiceField(label='Grasc *', choices=TRAB, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estatus_biblio = forms.ChoiceField(label='Estatus Biblioteca', choices=ALBA, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    otras_uts = forms.ChoiceField(label='Otras UTS *', choices=RESSN, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estatus_inscri_est = forms.ChoiceField(label='Estatus inscripción *', choices=CONTROL, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    id_tipo_esc_est = forms.ChoiceField(label='Tipo Escuela:',choices=TIPESC,widget=forms.Select(attrs={'class': 'form-control','style': 'border-color:#21B64A;'}))
    periodo_est = forms.ChoiceField(label='Periodo:',choices=PERIODOS,widget=forms.Select(attrs={'class': 'form-control','style': 'border-color:#21B64A;'}))
    turno_est = forms.ChoiceField(label='Turno*', choices=TURN, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    sexo_est = forms.ChoiceField(label='¿Sexo?*', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    trabaja_est = forms.ChoiceField(label='¿Trabajas?*', choices=TRAB, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estado_civil_est = forms.ChoiceField(label='Estado civil *', choices=EDOCIVIL, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    class Meta:
        model = SeTabEstudiante
        fields = '__all__'
        exclude = ('rowid_matricula', 'estatus_est')
        widgets = {
            'rowid_becas' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'rowid_car' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'rowid_col' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'rowid_grupo' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccionar datos', 'style' : 'border-color:#21B64A;'}),
            'id_matricula' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la matricula', 'style' : 'border-color:#21B64A;'}),
            'nombre_estu' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el o nombres del alumno ', 'style' : 'border-color:#21B64A;'}),
            'paterno_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el apellido paterno ', 'style' : 'border-color:#21B64A;'}),
            'materno_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el apellido materno', 'style' : 'border-color:#21B64A;'}),
            'rfc_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese RFC del estudiante', 'style' : 'border-color:#21B64A;'}),
            'curp_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el CURP del estudiante', 'style' : 'border-color:#21B64A;'}),
            'direccion_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la direccion del estudiante', 'style' : 'border-color:#21B64A;'}),
            'telefono_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el número telefonico', 'style' : 'border-color:#21B64A;'}),
            'email_est' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el correo personal del alumno', 'style' : 'border-color:#21B64A;'}),
            'fecha_alta_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la fecha DD/MM/AAAA', 'style' : 'border-color:#21B64A;'}),
            'user_alta_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el usuario que dio de alta.', 'style' : 'border-color:#21B64A;'}),
            'fecha_cambio_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese fecha DD/MM/AAAA', 'style' : 'border-color:#21B64A;'}),
            'user_cambio_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el ususario que modifico alumno', 'style' : 'border-color:#21B64A;'}),
            'codpos' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el código postal ', 'style' : 'border-color:#21B64A;'}),
            'fec_nac_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la fecha de nacimiento DD/MM/AAAA', 'style' : 'border-color:#21B64A;'}),
            'generacion_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la generacion del estudiante', 'style' : 'border-color:#21B64A;'}),
            'anio_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el año', 'style' : 'border-color:#21B64A;'}),
            'mat_tutor_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese apellido materno del tutor', 'style' : 'border-color:#21B64A;'}),
            'pat_tutor_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese apellido paterno del tutor', 'style' : 'border-color:#21B64A;'}),
            'nombre_tutor_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese nombre del tutor', 'style' : 'border-color:#21B64A;'}),
            'no_folio_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese no de folio del estudiante', 'style' : 'border-color:#21B64A;'}),
            'entidad_nac' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese entidad el numero de nacimiento', 'style' : 'border-color:#21B64A;'}),
            'mpo_del_nac' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese numero de municipio del estudiante', 'style' : 'border-color:#21B64A;'}),
            'tipo_sangre_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese tipo de sangre del estudiante', 'style' : 'border-color:#21B64A;'}),
            'id_area_bach_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el código del area de bachillerato', 'style' : 'border-color:#21B64A;'}),
            'entidad_bach': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el código de entidad del bachillerato', 'style' : 'border-color:#21B64A;'}),
            'mpo_del_bach' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el código del municipio', 'style' : 'border-color:#21B64A;'}),
            'fecha_ini_bach' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese año de inicio en bachillerato', 'style' : 'border-color:#21B64A;'}),
            'fecha_fin_bach' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese año de termino en bachillerato', 'style' : 'border-color:#21B64A;'}),
            'promedio_gral_bach' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese promedio general de bachillerato', 'style' : 'border-color:#21B64A;'}),
            'tel_trabajo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese telefono del trabajo del estudiante ', 'style' : 'border-color:#21B64A;'}),
            'edad_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese edad del estudiante', 'style' : 'border-color:#21B64A;'}),
            'fecha_vig_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese fecha de vigencia DD/MM/AAAA', 'style' : 'border-color:#21B64A;'}),
            'imss_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese numero del imms del estudiante', 'style' : 'border-color:#21B64A;'}),
            'clinica_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese número de clinica del estudiante', 'style' : 'border-color:#21B64A;'}),
            'num_servicio' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese número de servicio del estudiante', 'style' : 'border-color:#21B64A;'}),
            'fec_ser_social' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese fecha de servicio DD/MM/AAAA', 'style' : 'border-color:#21B64A;'}),
            'fecha_repos_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la fecha de reposicion DD/MM/AAAA. ', 'style' : 'border-color:#21B64A;'}),
            'matri_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la matricula del estudiante', 'style' : 'border-color:#21B64A;'}),
            'beca_pro_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el tipo de beca del estudiante', 'style' : 'border-color:#21B64A;'}),
            'usuario_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el usuario del estudiante', 'style' : 'border-color:#21B64A;'}),
            'password_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la contraseña del estudiante', 'style' : 'border-color:#21B64A;'}),
            'tipo_carrera_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el código de carrera del estudiante', 'style' : 'border-color:#21B64A;'}),
            'no_cedula_tsu' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el numero de cedula de TSU', 'style' : 'border-color:#21B64A;'}),
            'no_referencia' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el número de referencia', 'style' : 'border-color:#21B64A;'}),
            'institucion_seguro' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la institucion de seguro', 'style' : 'border-color:#21B64A;'}),
            'otrainstitucionseguro' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese si el estudiante tiene otra institucion del seguro', 'style' : 'border-color:#21B64A;'}),
            'nacionalidad' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la nacionalidad del estudiante', 'style' : 'border-color:#21B64A;'}),
            'tipodiscapacidad' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el tipo de discapacidad', 'style' : 'border-color:#21B64A;'}),
            'foliocertificado' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el número de folio de certificado', 'style' : 'border-color:#21B64A;'}),
            'fechaexpedicioncer' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese fecha de expedicion DD/MM/AAAA', 'style' : 'border-color:#21B64A;'}),
            'equivalencia' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la equivalencia', 'style' : 'border-color:#21B64A;'}),
            'parentescotutor' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el parentesco con el tutor', 'style' : 'border-color:#21B64A;'}),
            'num_int': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese numero interior', 'style' : 'border-color:#21B64A;'}),
            'num_ext' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese numero exterior', 'style' : 'border-color:#21B64A;'}),
            
        }
        labels = {
            'rowid_becas' : 'Becas *',
            'rowid_car' : 'Carrera *',
            'rowid_col' : 'Colonia *',
            'rowid_grupo' : 'Grupo *',
            'id_matricula' : 'Matricula *',
            'nombre_estu' : 'Nombre *',
            'paterno_est' : 'Apellido paterno*',
            'materno_est' : 'Apellido materno *',
            'rfc_est' : 'RFC *',
            'curp_est' : 'Curp *',
            'direccion_est' : 'Direccion *',
            'telefono_est' : 'Telefono *',
            'email_est' : 'Correo *',
            'fecha_alta_est': 'Fecha de alta *',
            'user_alta_est' : 'Usuario que registro*',
            'fecha_cambio_est' : 'Fecha de modificacion',
            'user_cambio_est' : 'Usuario que modifico',
            'codpos' : 'Código postal *',
            'fec_nac_est' : 'Fecha de nacimiento *',
            'generacion_est' : 'Generación *',
            'anio_est' : ' Año *',
            'mat_tutor_est' : 'Apellido materno del tutor *',
            'pat_tutor_est' : 'Apellido paterno del tutor *',
            'nombre_tutor_est' : 'Nombre(s) del tutor *',
            'no_folio_est' : 'Folio *',
            'entidad_nac' : 'Entidad de nacimiento *',
            'mpo_del_nac' : 'Municipio *',
            'tipo_sangre_est' : 'Tipo de sangre *',
            'id_area_bach_est' : 'Area bachillerato *',
            'entidad_bach': 'Entidad del bachillerato *',
            'mpo_del_bach' : 'Municipio del bachillerato *',
            'fecha_ini_bach' : 'Año de inicio *',
            'fecha_fin_bach' : 'Año de termino *',
            'promedio_gral_bach' : 'Promedio general bachillerato *',
            'tel_trabajo' : 'Telefono del trabajo',
            'edad_est' : 'Edad *',
            'fecha_vig_est' : 'Fecha de vigencia',
            'imss_est' : 'Numero del IMMS *',
            'clinica_est' : 'Clinica',
            'num_servicio' : 'Numero de servicio social *',
            'fec_ser_social' : 'Fecha de servicio social *',
            'fecha_repos_est' : 'Fecha de reposicion de credencial *',
            'matri_est' : 'Matricula *',
            'beca_pro_est' : 'Beca *',
            'usuario_est' : 'Usuario *',
            'password_est' : 'Contraseña *',
            'tipo_carrera_est' : 'Tipo carrera *',
            'no_cedula_tsu' : 'Cedula *',
            'no_referencia' : 'Referencia *',
            'institucion_seguro' : ' Institucion del seguro *',
            'otrainstitucionseguro' : 'Otra institucion del seguro ',
            'nacionalidad' : 'Nacionalidad *',
            'tipodiscapacidad' : 'Tipo de discapacidad ',
            'foliocertificado' : 'Folio certificado *',
            'fechaexpedicioncer' : 'Fecha de expedicion* ',
            'equivalencia' : 'Equivalencia *',
            'parentescotutor' : 'Parentesco tutor *',
            'num_int': 'Numero interior*',
            'num_ext' : 'Numero exterior *',
            
        }
##forms Documentacion
class FormDocumentacion(forms.ModelForm):
    CTGDOC = (
        ('0','Seleccione una opción'),
        ('TSU','TSU'),
        ('ING','ING'),
        ('OTRO','OTRO'),
    )
    DIFC = ( 
        ('0','Seleccione una opción'),
        ('A', 'Alta '), 
        ('M','Media'), 
        ('B','Baja') 
    )    
    importante_doc = forms.ChoiceField(label='Importancia del Documento *', choices=DIFC, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estatus_grado = forms.ChoiceField(label='Categoria del Documento', choices=CTGDOC, widget=forms.Select(attrs={'class':'form-control', 'style':'border-color:#21B64A;'}))
    class Meta:
        model = SeCatDocumentacion
        fields = '__all__'
        exclude = ('rowid_doc','estatus_doc',)
        widgets = {
            'id_doc' : forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese Clave del Documento',
                                                'style' : 'border-color:#21B64A;'}),
            'descri_largo_doc' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese nombre del Documento.',
                                                        'style' : 'border-color:#21B64A;'}),
            'descri_corto_doc' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese abreviatura del Documento.',
                                                        'style' : 'border-color:#21B64A;'}),
            'cve_control_doc' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese Clave de Control del Documento',
                                                        'style' : 'border-color:#21B64A;'}),
        }
        labels ={
            'id_doc' : 'Clave del Documento *',
            'descri_largo_doc' : 'Nombre del Documento *',
            'descri_corto_doc' : 'Abreviatura del Documento *',
            'cve_control_doc' : 'Clave de Control del Documento *',
        }
##forms Grupo
class FormGrupo(forms.ModelForm):
    class Meta:
        model = SeCatGrupo
        fields = '__all__'
        exclude = ('rowid_grupo','estatus_gpo',)
        widgets = {
            'rowid_car' : forms.Select(attrs={'class' : 'form-control',
                                                'style' : 'border-color:#21B64A;'}),
            'rowid_grado' : forms.Select(attrs={'class': 'form-control',
                                                'style' : 'border-color:#21B64A;'}),
            'id_grupo'  :  forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese clave del grupo',
                                                    'style' : 'border-color:#21B64A;'}),
            'descri_largo_gpo'  :  forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese nombre del grupo',
                                                            'style' : 'border-color:#21B64A;'}),
            'descri_corto_gpo'  :  forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese abreviatura del grupo',
                                                            'style' : 'border-color:#21B64A;'}),
            'lim_gpo'  :  forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Ingrese el número de alumnos',
                                                    'style' : 'border-color:#21B64A;'}),
            'lim_acu_gpo'  :  forms.NumberInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese el número máximo de alumnos',
                                                        'style' : 'border-color:#21B64A;'}),
            'lim_rec_gpo'  :  forms.NumberInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese el número de recursadores',
                                                        'style' : 'border-color:#21B64A;'}),
            'lim_acu_rec_gpo'  :  forms.NumberInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Ingrese el número máximo de recursadores',
                                                            'style' : 'border-color:#21B64A;'}),
        }
        labels = {
            'rowid_car' : 'Carrera',
            'rowid_grado' : 'Grado',
            'id_grupo'  :  'Clave del Grupo *',
            'descri_largo_gpo' : 'Nombre del Grupo *',
            'descri_corto_gpo' : 'Abreviatura del Grupo *',
            'lim_gpo' : 'Número de Alumnos',
            'lim_acu_gpo' : 'Máximo de Alumnos',
            'lim_rec_gpo' : 'Número de Recursadores',
            'lim_acu_rec_gpo' : 'Máximo de Recursadores',
        }
##forms Estatus estudiante
class FormEstatusEstudiante(forms.ModelForm):
    class Meta:
        model = SeCatEstatusEstudiante
        fields = '__all__'
        exclude = ('rowid_evento_est','estatus_tipo_est',)
        widgets = {
            'id_evento_est' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese clave del evento',
                                                        'style' : 'border-color:#21B64A;'}),
            'consecutivo_est' : forms.NumberInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el numero consecutivo',
                                                            'style' : 'border-color:#21B64A;'}),
            'descri_largo_tipo_est' : forms.TextInput(attrs={'class': 'form-control',
                                                                'required' : 'True',
                                                                'placeholder': 'Ingrese el nombre',
                                                                'style' : 'border-color:#21B64A;'}),
            'descri_corto_tipo_est' :forms.TextInput(attrs={'class': 'form-control',
                                                                'required' : 'True',
                                                                'placeholder': 'Ingrese la abreviatura',
                                                                'style' : 'border-color:#21B64A;'}),
        }
        labels ={
            'id_evento_est' : 'Clave Evento *',
            'consecutivo_est' :  'Consecutivo *',
            'descri_largo_tipo_est' : ' Nombre *',
            'descri_corto_tipo_est' : 'Abreviatura *'
        }
# Forms SALONES
class FormSalones(forms.ModelForm):
    TIPOSALON = (
        (0,'Seleccione una opción'),
        (1,'Clase frente a grupo'),
        (2,'Conferencia'),
        (3,'Laboratorio')
    )
    tipo_salon = forms.ChoiceField(label='Tipo Salón:', choices=TIPOSALON, widget=forms.Select(attrs={'class':'form-control', 'style':'border-color:#21B64A;'}))
    COMPARTIDO = (
        (0,'Seleccione una opción'),
        (1,'Si'),
        (2,'No'),
    )
    compartido_salon = forms.ChoiceField(label='Compartido:', choices=COMPARTIDO, widget=forms.Select(attrs={'class':'form-control', 'style':'border-color:#21B64A;'}))
    class Meta:
        model= SeCatSalones
        fields= '__all__'
        exclude = ('rowid_salon', 'estatus_salon')
        widgets = {
            'rowid_car': forms.Select(attrs={'class': 'form-control',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'id_salon': forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese clave del Salón.',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'descri_largo_salon': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese nombre del Salón.',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'descri_corto_salon': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese abreviatura del Salón.',
                                                'style' : 'border-color:#21B64A;'
                                                }),
        }
        labels = {
                'rowid_car' : 'Carrera',
                'id_salon' : 'Clave del Salón *',
                'descri_largo_salon' : 'Nombre del Salón',
                'descri_corto_salon' : 'Abreviatura del Salón',
        }
# Forms GRADOS
class FormGrados(forms.ModelForm):
    class Meta:
        model= SeCatGrado
        fields= '__all__'
        exclude = ('rowid_grado', 'estatus_gra')
        widgets = {
            'id_grado': forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese clave del grado.',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'descri_corto_gra' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el grado.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'id_grado' : 'Clave del Grado *',
                'descri_corto_gra' : 'Nombre del Grado *',
        }
# Forms BECAS
class FormBecas(forms.ModelForm):
    class Meta:
        model = SeCatBecas
        fields = '__all__'
        exclude = ('rowid_becas', 'estatus_bec')
        widgets = {
            'id_becas':  forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese clave de la Beca',
                                                        'style' : 'border-color:#21B64A;'
                                              }),
            'valor_ini_bec': forms.NumberInput(attrs={'class': 'form-control','required': 'True',
                                                    'placeholder': 'Ingrese valor inicial de la Beca.',
                                                    'required' : 'True',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'valor_fin_bec': forms.NumberInput(attrs={'class': 'form-control','required': 'True',
                                                    'placeholder': 'Ingrese valor final de la Beca.',
                                                    'required' : 'True',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'porcentaje_beca': forms.NumberInput(attrs={'class': 'form-control','required': 'True',
                                                      'placeholder': 'Ingrese porcentaje de la Beca.',
                                                      'required' : 'True',
                                                      'style' : 'border-color:#21B64A;'
                                                      }),
        }
        labels = {
                'id_becas':'Clave Beca *',
                'valor_ini_bec': 'Valor Inicial. *',
                'valor_fin_bec': 'Valor Final. *',
                'porcentaje_beca': 'Porcentaje. *',
        }
#Forms Tipos Cambios
class FormTipoCambio(forms.ModelForm):
    class Meta:
        model = SeCatTipoCambio
        fields = '__all__'
        exclude = ('rowid_tipo_cambio', 'status')
        widgets = {
            'id_tipo_cambio':  forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese clave del Tipo Cambio',
                                                        'style' : 'border-color:#21B64A;'
                                              }),
            'descri_tipocambio': forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingresa Descripción del Tipo Cambio',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'id_tipo_cambio': 'Clave del Tipo Cambio *',
                'descri_tipocambio': 'Descripción del Tipo Cambio *',
        }
#Forms Tipos baja
class FormTipoBajas(forms.ModelForm):
    class Meta:
        model = SeCatTipoBajas
        fields = '__all__'
        exclude = ('rowid_tipo_baj', 'estatus_tipo_baj')
        widgets = {
            'id_tipo_baj':  forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese clave del Tipo Cambio',
                                                        'style' : 'border-color:#21B64A;'
                                              }),
            'descri_largo_tipo_baj': forms.TextInput(attrs={'class': 'form-control', 
                                                            'placeholder': 'Ingrese nombre del tipo de baja',
                                                            'style' : 'border-color:#21B64A;',
                                                            'required' : 'True'
                                                            }),
            'descri_corto_tipo_baj': forms.TextInput(attrs={'class': 'form-control', 
                                                            'placeholder': 'Ingrese abreviatura del tipo de baja',
                                                            'style' : 'border-color:#21B64A;',
                                                            'required' : 'True'
                                                            }),
        }
        labels = {
                'id_tipo_baj': 'Clave Tipo de Bajas *',
                'descri_largo_tipo_baj': 'Nombre Tipo de Bajas *',
                'descri_corto_tipo_baj': 'Abreviatura Tipo de bajas *',
            }

# -------------------------------------------- Empleado --------------------------------------------- #

######################## EMPLEADOS ############################
#forms empleados
class FormEmpleado(forms.ModelForm):
    VAL = ( ('A', 'Alta'), ('B','Baja') )
    EDOCIVIL = ( ('S', 'Soltero'), ('C','Casado'), ('V','Viudo'), ('D','Divorciado') )
    BIBLIO = ( ('A', 'Alta'), ('B','Baja') )
    SEXO = ( ('M', 'Masculino'), ('F', 'Femenino') )
    TCON = ( (1, 'Temporal'), (2,'Permanente') )
    ESCOMP = (('A', 'Alta'), ('B','Baja'))
    sexo_emp = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estatus_val = forms.ChoiceField(label='Estatus Val', choices=VAL, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estado_civil_emp = forms.ChoiceField(label='Estado Civil', choices=EDOCIVIL, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estatus_biblio = forms.ChoiceField(label='Estatus Biblioteca', choices=BIBLIO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    tipo_contrato_com = forms.ChoiceField(label='Tipo de Contrato', choices=TCON, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estatus_comp = forms.ChoiceField(label='Estatus Comp', choices=ESCOMP, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    class Meta:
        model = SeCatEmpleado
        fields = '__all__'
        exclude = ('rowid_empleado', 'estatus_emp')
        widgets = {
            'rowid_academico': forms.Select(attrs={'class': 'form-control',  
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }),
            'rowid_car': forms.Select(attrs={'class': 'form-control',  
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'rowid_depto': forms.Select(attrs={'class': 'form-control', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }),
            'rowid_edo': forms.Select(attrs={'class': 'form-control',  
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }),
            'rowid_col': forms.Select(attrs={'class': 'form-control', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'rowid_sueldo': forms.Select(attrs={'class': 'form-control', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'id_empleado': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el ID del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }),
            'nombre_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el nombre del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'paterno_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el apellido paterno del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'materno_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el apellido materno del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'rfc_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el RFC del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'curp_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el CURP del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'direccion_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese la direccion del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'telefono_emp': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el telefono del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'email_emp': forms.EmailInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el email del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'fecha_alta_emp': forms.DateInput(attrs={'class': 'form-control', 
                                                        'placeholder':'DD/MM/AAAA', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'user_alta_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el usuario del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'user_cambio_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el cambio de usuario del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'fecha_cambio_emp': forms.DateInput(attrs={'class': 'form-control', 
                                                        'placeholder':'DD/MM/AAAA', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }),  
            'codpos_emp': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese codigo postal del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'horas_contra_emp': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese las horas de contrato del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }),
            'fec_nac_emp': forms.DateInput(attrs={'class': 'form-control', 
                                                        'placeholder':'DD/MM/AAAA', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'edad_emp': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese la edad del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'num_vac_max': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese ', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'num_vac_act': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese ', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'cedula_emp_com': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese la cedula del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'fecicon': forms.DateInput(attrs={'class': 'form-control', 
                                                        'placeholder':'DD/MM/AAAA', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'fecfcon': forms.DateInput(attrs={'class': 'form-control', 
                                                        'placeholder':'DD/MM/AAAA', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'comentario_emp': forms.Textarea(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese un comentario', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
        }
        labels = {
                'rowid_academico':'Nivel Academico *',
                'rowid_car':'Carrera *', 
                'rowid_depto':'Departamento *',
                'rowid_edo' :'Estado de Nacimiento *', 
                'rowid_col':'Colonia *',  
                'rowid_sueldo':'Sueldo *', 
                'id_empleado':'ID Empleado *',
                'nombre_emp':'Nombre *', 
                'paterno_emp':'Apellido Paterno *', 
                'materno_emp':'Apellido Materno *', 
                'rfc_emp':'RFC *', 
                'curp_emp':'CURP *', 
                'direccion_emp':'Direccion *', 
                'telefono_emp':'Telefono *', 
                'email_emp':'Email', 
                'fecha_alta_emp':'Fecha de ALta',
                'user_alta_emp':'Usuario de Alta',
                'user_cambio_emp':'Usuario que modifico',
                'fecha_cambio_emp':'Fecha de Cambio',
        #         'fecha_alta_emp':'fecha cuando se dio de alta', 
        #         'user_alta_emp':'quien lo dio de alta', 
        #         'user_cambio_emp':'quien hizo los cambios', 
        #         'fecha_cambio_emp':'fecha cuando hizo los cambios',  
                'codpos_emp':'Codigo Postal',
                'horas_contra_emp':'Horas de Contrato', 
        #         'horas_contra_emp':'horas contratadas (lo asigna la division)',
                'fec_nac_emp':'Fecha de Nacimiento', 
                'estatus_comp':'Estatus Comp',
        #         'estatus_val':'estos estatus son dependiendo los roles',(Rh y division) 
        #         'estatus_comp':'S', 
                'edad_emp':'Edad', 
                'num_vac_max':'Numero Maximo de Vacaciones',
                'num_vac_act':'Numero de Vacaciones Actuales',
        #         'num_vac_max':'numero de vacaciones', 
        #         'num_vac_act':'actuales', 
        #         'tipo_contrato_com':'1, permante, 2 temporal',
                'cedula_emp_com':'Cedula Profesional', 
                'fecicon':'Fecha de Inicio de Contrato',
                'fecfcon':'Fecha Final de Contrato',
        #         'fecicon':'inicio', 
        #         'fecfcon':'fin contrato', 
                'comentario_emp':'Comentario',
        #         'estatus_biblio':'estatus val, ',
            }
# Form Nivel Academico
class FormNivAca(forms.ModelForm):
    class Meta:
        model = SeCatNivelAcademico
        field = '__all__'
        exclude = ('estatus_acade',)
        widgets = {
            'id_academico': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Ingrese el ID de Nivel Academico *',
                                                        'required' : 'True', 
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_largo_acade': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el Nivel Academico *',
                                                        'required' : 'True', 
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_corto_acade': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese la Abreviatura *',
                                                        'required' : 'True', 
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'id_academico' : 'ID de Nivel Academico *',
                'descri_largo_acade': 'Nivel Academico *',
                'descri_corto_acade': 'Abreviatura *',
            }
#Forms Plaza
class FormPlaza(forms.ModelForm):
    class Meta:
        model = SeCatPlaza
        field = '__all__'
        exclude = ('estatus_plaza',)
        widgets = {
            'id_plaza': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Ingrese ID de la plaza',
                                                        'required' : 'True', 
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_largo_plaza': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Ingrese nombre de la plaza',
                                                        'required' : 'True', 
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_corto_plaza': forms.TextInput(attrs={'class':'form-control', 
                                                        'placeholder': 'Ingrese la abreviatura',
                                                        'required' : 'True', 
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'id_plaza': 'ID Plaza *',
                'descri_largo_plaza': 'Nombre de Plaza *',
                'descri_corto_plaza': 'Abreviatura *',
            }
# Froms TIPO PUESTO
class FormsTipoPue(forms.ModelForm):
    class Meta:
        model= SeCatTipoPuesto
        fields= '__all__'
        exclude = ('estatus_pue',)
        widgets = {
            'rowid_plaza': forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Seleccione la Plaza.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'id_puesto': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la clave del Puesto',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_largo_pue': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el Puesto',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'descri_corto_pue' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la abreviacion del Puesto',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
                'rowid_plaza':'Plaza *',
                'id_puesto':'ID del Puesto *',
                'descri_largo_pue':'Puesto *',
                'descri_corto_pue' : 'Abreviacion *',
        }
# Froms Sueldos
class FormSueldo(forms.ModelForm):
    class Meta:
        model= SeCatSueldos
        fields= '__all__'
        exclude = ('rowid_sueldo','estatus_sueldo')
        widgets = {
            'rowid_puesto' : forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'id_sueldo': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el ID del sueldo.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el sueldo.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }

        labels = {

                'rowid_puesto' : 'Puesto *',
                'id_sueldo': 'ID del Sueldo *',
                'sueldo': 'Sueldo *',
        }
# FORM Adscripciones
class FormAdscripcion(forms.ModelForm):
    class Meta:
        model = SeCatDeptoEmp
        fields = '__all__'
        exclude = ('rowid_depto', 'estatus_depto')          
        widgets = {
            'id_depto': forms.TextInput(attrs={'class': 'form-control',
                                            'required' : 'True',
                                             'placeholder': 'Ingrese la clave',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'conse_depto': forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el num. consecutivo',
                                                'style' : 'border-color:#21B64A;'
                                                }),
            'descri_largo_dep_emp': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre departamento.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
            'descri_corto_dep_emp': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la abreviatura.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
            'titular_depto': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese el Titular.',
                                                'style' : 'border-color:#21B64A;'                                                
                                                }),
            'clave_ser': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese la Clave servicio.',
                                                'style' : 'border-color:#21B64A;'                                                
                                                }),
        }
        labels = {
            'id_depto': 'Clave.depto *',
            'conse_depto': 'Consecutivo.depto *',
            'descri_largo_dep_emp': 'Nombre departamento *',
            'descri_corto_dep_emp': 'Abreviatura *',
            'titular_depto': 'Titular.',
            'clave_ser': 'Clave servicio.',
        }
# FORM Actividades
class FormActividades(forms.ModelForm):
    class Meta:
        model = SeCatActividades
        fields = '__all__'
        exclude = ('rowid_actividad', 'estatus_act')          
        widgets = {
            'id_actividad': forms.NumberInput(attrs={'class': 'form-control',
                                            'required' : 'True',
                                             'placeholder': 'Ingrese la clave',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'descri_largo_act': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre de la Actividad.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
            'descri_corto_act': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la abreviatura.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
        }
        labels = {
            'id_actividad': 'Clave *',
            'descri_largo_act': 'Actividad *',
            'descri_corto_act': 'Abreviatura *',
        }
# FORM Institucion
class FormInstitucion(forms.ModelForm):  
    class Meta:
        model = SeCatInstitucion
        fields = '__all__'
        exclude = ('rowid_institucion', 'estatus_ins')          
        widgets = {
            'id_institucion': forms.NumberInput(attrs={'class': 'form-control',
                                            'required' : 'True',
                                             'placeholder': 'Ingrese la clave',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'descri_largo_ins': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre de la Institucion.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
            'descri_corto_ins': forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la abreviatura.',
                                                        'style' : 'border-color:#21B64A;'                                                        
                                                        }),
        }
        labels = {
            'id_institucion': 'Clave *',
            'descri_largo_ins': 'Institución *',
            'descri_corto_ins': 'Abreviatura *',
        }
# FORM Carrera Empleado
class FormEmpCar(forms.ModelForm):  
    class Meta:
        model = SeTabEmpCar
        fields = '__all__'
        exclude = ('rowid_emp_car', 'estatus_inst')          
        widgets = {
            'rowid_institucion': forms.Select(attrs={'class': 'form-control',
                                            'required' : 'True',
                                            'initial':'FIXED',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'rowid_empleado': forms.Select(attrs={'class': 'form-control',
                                            'required' : 'True',
                                            'style' : 'border-color:#21B64A;'
                                            }),
            'descri_largo_car_emp': forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el nombre de la carrera .',
                                                    'style' : 'border-color:#21B64A;'                                                        
                                                    }),
            'descri_corto_car_emp': forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese la abreviatura.',
                                                    'style' : 'border-color:#21B64A;'                                                        
                                                    }),
        }
        labels = {
            'rowid_empleado': 'Empleado *',
            'rowid_institucion': 'Institución *',
            'descri_largo_car_emp': 'Carrera*',
            'descri_corto_car_emp': 'Abreviatura *',
        }

# -------------------------------------------- Operaciones --------------------------------------------- #

##########################  Operaciones #################################
# Froms Aspirantes
class FormsAspirantes(forms.ModelForm):
    SEXO = ( ('M', 'Masculino'), ('F', 'Femenino') )
    EDOCIVIL = ( ('S', 'Soltero'), ('C','Casado'), ('V','Viudo'), ('D','Divorciado') )
    TRAB = ( ('S', 'Si'), ('N','No') )
    TESC = ( (1, 'Pública'), (2,'Privada') )
    PERIODOS = ((0,'Seleccione el Periodo'),(1,'Enero-Abril'),(2,'Mayo-Agosto'),(3,'Septiembre-Diciembre'))
    TURNO = ( ('M','Matutino'), ('V','Vespertino') )
    DIS = ( ('S', 'Si'), ('N','No') )
    SERMED = ( ('S', 'Si'), ('N','No') )
    IND = ( ('S', 'Si'), ('N','No') )
    sexo_asp = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estado_civil_asp = forms.ChoiceField(label='Estado Civil', choices=EDOCIVIL, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    trabaja_asp = forms.ChoiceField(label='Trabaja', choices=TRAB, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    tipo_publica_privada = forms.ChoiceField(label='Tipo de Escuela', choices=TESC, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    periodo_asp = forms.ChoiceField(label='Periodo:',choices=PERIODOS,widget=forms.Select(attrs={'class': 'form-control','style': 'border-color:#21B64A;'}))
    turno_asp = forms.ChoiceField(label='Turno', choices=TURNO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    discapacidad = forms.ChoiceField(label='Discapacidad', choices=DIS, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    serviciomedico = forms.ChoiceField(label='Servicio Medico', choices=SERMED, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    indigena = forms.ChoiceField(label='Indigena', choices=IND, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    class Meta:
        model= SeTabAspirante
        fields= '__all__'
        exclude = ('estatus_asp',)
        widgets = {
            'folio_utn_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el folio del aspirante',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'rowid_area_bac' :  forms.Select(attrs={'class': 'form-control',
                                                                    'required' : 'True',
                                                                    'style' : 'border-color:#21B64A;'
                                                                    }),
            'rowid_medio_dif' : forms.Select(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
            'rowid_car' : forms.Select(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'rowid_tipo_esc' : forms.Select(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'rowid_col' : forms.Select(attrs={'class': 'form-control',
                                              'required' : 'True',
                                              'style' : 'border-color:#21B64A;'
                                               }), 
            'fecha_alt_asp' : forms.DateInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'DD/MM/AAAA',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'mpo_o_alcaldia_nac_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el Municipio o Alcaldia',
                                                            'style' : 'border-color:#21B64A;'
                                                            }),
            'ent_fed_nac_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el Estado',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'calle_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese la calle',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'num_int_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el numero interior',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'num_ext_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el numero exterior',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'codigo_postal_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el Codigo Postal',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'tel_cas_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el Telefono',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'telefono_oficina_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el Telefono de Oficina',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'edad_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese la edad del aspirante',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'tipo_de_sangre_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el tipo de sangre',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'promedio_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el promedio',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'fecini_bach_asp' : forms.DateInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre del plan',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'fecfin_bach_asp' : forms.DateInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'DD/MM/AAAA',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'rfc_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'DD/MM/AAAA',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'curp_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el CURP',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'nom_esc_pro_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la escuela de procedencia',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'fecha_nac_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese la fecha de nacimiento',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'materno_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el apellido materno',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'paterno_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el apellido paterno',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'nombre_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el nombre del aspirante',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'folio_cen_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el folio',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),  
            'anio_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el año',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'mat_tutor_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el apellido materno del tutor del aspirante',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'pat_tutor_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el apellido paterno del tutor del aspirante',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'nombre_tutor_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre del tutor del aspirante',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'generacion_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la generacion',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'entidad_estudio' : forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la entidad de estudio',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'municipio_estudio' : forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre del plan',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'ronda_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese la ronda',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'user_alta' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el nombre del usuario',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'user_cambio' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el nombre del usuario',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'email_asp' : forms.EmailInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el email',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'opcioneducativa' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la opcion educativa',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'continuidadestudio' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese la continuidad de estudios',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'otromediodif' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese otro medio de difusion',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'otromedioinf' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese otro medio de informacion',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'otroopcioneduca' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese otra opcion educativa',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'facebook' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el Facebook',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'twitter' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el Twitter',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'tipodiscapacidad' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el tipo de discapacidad',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'institucionseguro' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la institucion del seguro',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'otrainstitucionseguro' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese otra institucion de seguro',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'numafiliacion' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el numero de afiliacion',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'fechaexpedicioncer' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese la fecha de expedicioin de certificado',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'folio' : forms.TextInput(attrs={'class': 'form-control',
                                            'required' : 'True',
                                            'placeholder': 'Ingrese el folio',
                                            'style' : 'border-color:#21B64A;'
                                            }), 
            'fechacompromisocerti' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese la fecha de compromiso del certificado',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'poblacionindigena' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la poblacion indigena',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'lenguaindigena' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la lengua indigena que habla',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
            'folio_utn_asp' : 'Folio del Aspirante *', 
            'rowid_area_bac' : 'Area de Bachillerato *',
            'rowid_medio_dif' : 'Medio de Difusion *',
            'rowid_car' : 'Carrera *',
            'rowid_tipo_esc' : 'Tipo Escuela *',
            'rowid_col' : 'Colonia *',
            'fecha_alt_asp' : 'Fecha de Alta *' ,
            'mpo_o_alcaldia_nac_asp' : 'Municipio/Alcaldia de Nacimiento del Aspirante *',
            'ent_fed_nac_asp' : 'Estado de Nacimiento del Aspirante *' ,
            'calle_asp' : 'Calle del Aspirante *' ,
            'num_int_asp' : 'Numero Interior ' ,
            'num_ext_asp' : 'Numero Exterior *',
            'codigo_postal_asp' : 'Codigo Postal *', 
            'tel_cas_asp' : 'Telefono de Casa del Aspirante *', 
            'telefono_oficina_asp' : 'Telefono de Oficina del Aspirante *', 
            'edad_asp' : 'Edad del Aspirante *'  ,
            'tipo_de_sangre_asp' : 'Tipo de Sangre del Aspirante *',
            'promedio_asp' : 'Promedio del Aspirante *' ,
            'fecini_bach_asp' : 'Fecha de Inicio de Bachillerato del Aspirante *', 
            'fecfin_bach_asp' : 'Fecha de Termino de Bachillerato del Aspirante *',
            'rfc_asp' : 'RFC del Aspirante *' ,
            'curp_asp' : 'CURP del Aspirante *', 
            'nom_esc_pro_asp' : 'Nombre de escuela de Procedencia *', 
            'fecha_nac_asp' : 'Fecha de Nacimiento del Aspirante *' ,
            'materno_asp' : 'Apellido Materno del Aspirante *' ,
            'paterno_asp' : 'Apellido Paterno del Aspirante *',
            'nombre_asp' : 'Nombre del Aspirante *'  ,
            'folio_cen_asp' : 'Folio Cen del Aspirante *', 
            'anio_asp' : 'Año del Aspirante *',
            'mat_tutor_asp' : 'Apellido Materno del Tutor del Aspirante *', 
            'pat_tutor_asp' : 'Apellido Paterno del Tutor del Aspirante *' ,
            'nombre_tutor_asp' : 'Nombre del Tutor del Aspirante *',
            'generacion_asp' : 'Generacion del Aspirante ',
            'entidad_estudio' : 'Entidad de Estudio del Aspirante ', 
            'municipio_estudio' : 'Municipio de Estudio del Aspirante *', 
            'ronda_asp' : 'Ronda del Aspirante ',
            'user_alta' : 'Usuario que dio de alta ', 
            'user_cambio' : 'Usuario que hizo cambios ', 
            'email_asp' : 'Email del Aspirante ' ,
            'opcioneducativa' : 'Opcion Educativa ', 
            'continuidadestudio' : 'Continuidad Estudio ', 
            'otromediodif' : 'Otro medio de Difusion ' ,
            'otromedioinf' : 'Otro medio de Informacion ', 
            'otroopcioneduca' : 'Otra opcion Educativa ' ,
            'facebook' : 'Facebook ' ,
            'twitter' : 'Twitter ' ,
            'tipodiscapacidad' : 'Tipo de discapacidad '  ,
            'institucionseguro' : 'Institucion de seguro del Aspirante ', 
            'otrainstitucionseguro' : 'Otra Institucion de Seguro ' ,
            'numafiliacion' : 'Numero de afiliacion ' ,
            'fechaexpedicioncer' : 'Fecha de Expedicion del Certificado ', 
            'folio' : 'Folio del Aspirante ' ,
            'fechacompromisocerti' : 'Fecha de Compromiso de Certificado ', 
            'poblacionindigena' : 'Poblacion Indigena ',
            'lenguaindigena' : 'Lengua Indigena ',
        }