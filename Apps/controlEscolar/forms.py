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
    SeTabAspirante, SeProAspDocu, SeTabAceptados,  # Operaciones / Aspirante
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

    rowid_pais = forms.ModelChoiceField(queryset = SeCatPais.objects.filter(estatus_pais="A"),
                                  required=True,
                                  label="Pais: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    
    class Meta:
        model = SeCatEstado
        fields = '__all__'
        exclude = ('rowid_edo', 'estatus_edo',)
        widgets = {
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
                'id_edo': 'Clave Estado: *',
                'descri_largo_edo': 'Estado: *',
                'descri_corto_edo': 'Abreviatura: *',
        }
# Form Municipios/Delegaciones 
class FormMunicipiosDelegaciones(forms.ModelForm):
    rowid_edo = forms.ModelChoiceField(queryset = SeCatEstado.objects.filter(estatus_edo="A"),
                                  required=True,
                                  label="Estado: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatMunicipioDelegacion
        fields = '__all__'
        exclude = ('rowid_mundel','estatus_mundel')

        widgets = {
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
    rowid_mundel = forms.ModelChoiceField(queryset = SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A"),
                                  required=True,
                                  label="Municipio/Alcaldía:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_asentamiento = forms.ModelChoiceField(queryset = SeCatAsentamiento.objects.filter(estatus_asentamiento="A"),
                                  required=True,
                                  label="Asentamiento: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatColonia
        fields = '__all__'
        exclude = ('rowid_col', 'estatus_col') 
        widgets = {
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
            'id_col': 'Clave *',
            'descri_largo_col': 'Colonia *',
            'descrip_corto_col': 'Abreviatura *',
            'codposcol': 'Codigo Postal.',
        }

# -------------------------------------------- Universidad --------------------------------------------- #

# Form Universidad
class FormUniversidad(forms.ModelForm):
    rowid_col = forms.ModelChoiceField(queryset = SeCatColonia.objects.filter(estatus_col="A"),
                                  required=True,
                                  label="Colonia: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatUniversidad
        fields = '__all__'
        exclude = ('rowid_uni', 'estatus_uni')
        widgets = {
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
    rowid_uni = forms.ModelChoiceField(queryset = SeCatUniversidad.objects.filter(estatus_uni="A"),
                                  required=True,
                                  label="Universidad: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatDivision
        fields = '__all__'
        exclude = ('rowid_div', 'estatus_div')
        widgets = {
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
    rowid_div = forms.ModelChoiceField(queryset = SeCatDivision.objects.filter(estatus_div="A"),
                                  required=True,
                                  label="Division: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatCarrera
        fields = '__all__'
        exclude = ('estatus_car','rowid_car' )
        widgets = {
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
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatPeriodos
        field = '__all__'
        exclude = ('rowid_per','estatus_per')
        widgets = {
            'evento_per': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese evento','style': 'border-color:#21B64A;'}),
            'consecutivo_per': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingrese consecutivo','style': 'border-color:#21B64A;'}),
            'fecha_inicial_per': forms.DateInput(attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA','style': 'border-color:#21B64A;'}),
            'fecha_final_per': forms.DateInput(attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA','style': 'border-color:#21B64A;'}),
            'anio_per': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingresa el año','style': 'border-color:#21B64A;'}),
            'descripcion_per': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese descripcion de la plaza','style': 'border-color:#21B64A;'}),
        }
        labels = {
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
    rowid_plan_est = forms.ModelChoiceField(queryset = SeCatPlaEstudio.objects.filter(estatus_plan_est="A"),
                                  required=True,
                                  label="Plan de Estudio: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatAsignatura
        fields = '__all__'
        exclude = ('rowid_asignatura','estatus_asi',)
        widgets = {
            'id_asignatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el nombre de la Asignatura', 'style' : 'border-color:#21B64A;'}),
            'descri_larga_asi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el nombre de la Asignatura', 'style' : 'border-color:#21B64A;'}),
            'descri_corto_asi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la abreviatura del Asignatura', 'style' : 'border-color:#21B64A;'}),
        }
        labels = {
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
    rowid_asignatura = forms.ModelChoiceField(queryset = SeCatAsignatura.objects.filter(estatus_asi="A"),
                                  required=True,
                                  label="Asignatura: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_plan_est = forms.ModelChoiceField(queryset = SeCatPlaEstudio.objects.filter(estatus_plan_est="A"),
                                  required=True,
                                  label="Plan de Estudio: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_grado = forms.ModelChoiceField(queryset = SeCatGrado.objects.filter(estatus_gra="A"),
                                  required=True,
                                  label="Grado: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeProPlanEstudio
        fields = '__all__'
        exclude = ('rowid_pro_plan_est','estatus_pea',)
        widgets = {
            'horas_plan_est' :  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese las horas', 'style' : 'border-color:#21B64A;'}),
            'creditos_plan_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese los creditos', 'style' : 'border-color:#21B64A;'}), 
            'nota_minima_apro_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la nota minima', 'style' : 'border-color:#21B64A;'}),
            'valor_pon_final' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el valor final', 'style' : 'border-color:#21B64A;'}),
        }
        labels = {
            'horas_plan_est' : 'Numero de horas',
            'creditos_plan_est' : 'Creditos ',
            'nota_minima_apro_est' : 'Nota minima aprobatoria',
            'valor_pon_final' : 'Valor final',
        }
#Plan de estudio asignatura indicador
class FormsPeaI(forms.ModelForm):
    rowid_pro_plan_est = forms.ModelChoiceField(queryset = SeProPlanEstudio.objects.filter(estatus_pea="A"),
                                  required=True,
                                  label="Plan de Estudio: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_indicador = forms.ModelChoiceField(queryset = SeCatIndicador.objects.filter(estatus_ind="A"),
                                  required=True,
                                  label="Indicador: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeProAsiIndicador
        fields = '__all__'
        exclude = ('rowid_pro_asi_ind', 'estatus_peai',)
        widgets = {
            'porcentaje_pro_asi_idi' :  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el porcentaje', 'style' : 'border-color:#21B64A;'}),
            'comen_pro_asi_ind'  :  forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el comentario', 'style' : 'border-color:#21B64A;'}),    
        }
        labels = {
            'porcentaje_pro_asi_idi' : 'Porcentaje',
            'comen_pro_asi_ind' : 'Comentario',
        }

# -------------------------------------------- Aspirantes --------------------------------------------- #

################## Escuela Procedencia ########################
class FormEscProc(forms.ModelForm):
    rowid_mundel = forms.ModelChoiceField(queryset = SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A"),
                                  required=True,
                                  label="Municipio/Alcaldía:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatEscuelaProcedencia
        fields = '__all__'
        exclude = ('estatus_esc_proc','rowid_esc_proc')
        widgets = {
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
    rowid_col = forms.ModelChoiceField(queryset = SeCatColonia.objects.filter(estatus_col="A"),
                                  required=True,
                                  label="Colonia: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatTipoEscuela
        fields = '__all__'
        exclude = ('rowid_tipo_esc', 'estatus_esc')
        widgets = {
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
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_indicador = forms.ModelChoiceField(queryset = SeCatIndicador.objects.filter(estatus_ind="A"),
                                  required=True,
                                  label="Indicador: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model= SeProIndAsp
        fields= '__all__'
        exclude = ('rowid_pro_ind_asp', 'estatus_indicadores')
        widgets = {
            'valor_porcentual': forms.NumberInput(attrs={'class': 'form-control',
                                                        'required': 'True',
                                                        'placeholder': 'Ingrese valor porcentual del Indicador Aspirante.',
                                                        'required' : 'True',
                                                        'style' : 'border-color:#21B64A;'
                                                    }),
        }
        labels = {
                'valor_porcentual' : 'Valor porcentual del Indicador Aspirante *',
        }

# -------------------------------------------- Estudiantes --------------------------------------------- #

##forms ESTUDANTE
class FormsEstudiante(forms.ModelForm): # beca_pro_est
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
    BECA = ( ('S', 'Si'), ('N','No') )
    TIPOCARRERA = ( ('1', 'TSU'), ('2','INGENIARIA') )
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
    beca_pro_est = forms.ChoiceField(label='Otro tipo de Beca*', choices=BECA, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    tipo_carrera_est = forms.ChoiceField(label='Tipo Carrera*', choices=TIPOCARRERA, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))

    rowid_becas = forms.ModelChoiceField(queryset = SeCatBecas.objects.filter(estatus_bec="A"),
                                  required=True,
                                  label="Becas: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_mundel = forms.ModelChoiceField(queryset = SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A"),
                                  required=True,
                                  label="Municipio/Alcaldía:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_col = forms.ModelChoiceField(queryset = SeCatColonia.objects.filter(estatus_col="A"),
                                  required=True,
                                  label="Colonia: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_esc_proc = forms.ModelChoiceField(queryset = SeCatEscuelaProcedencia.objects.filter(estatus_esc_proc="A"),
                                  required=True,
                                  label="Escuela de Procedencia: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_grupo = forms.ModelChoiceField(queryset = SeCatGrupo.objects.filter(estatus_gpo="A"),
                                  required=True,
                                  label="Grupo: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeTabEstudiante
        fields = '__all__'
        exclude = ('rowid_matricula', 'estatus_est')
        widgets = {
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
            'tipo_sangre_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese tipo de sangre del estudiante', 'style' : 'border-color:#21B64A;'}),
            'id_area_bach_est' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el código del area de bachillerato', 'style' : 'border-color:#21B64A;'}),
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
            'usuario_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese el usuario del estudiante', 'style' : 'border-color:#21B64A;'}),
            'password_est' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Por favor, Ingrese la contraseña del estudiante', 'style' : 'border-color:#21B64A;'}),
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
            'id_matricula' : 'Id Matricula*',
            'nombre_estu' : 'Nombre *',
            'paterno_est' : 'Apellido paterno*',
            'materno_est' : 'Apellido materno *',
            'rfc_est' : 'RFC *',
            'curp_est' : 'Curp *',
            'direccion_est' : 'Direccion*',
            'telefono_est' : 'Telefono*',
            'email_est' : 'Correo*',
            'fecha_alta_est': 'Fecha*',
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
            'tipo_sangre_est' : 'Tipo de sangre *',
            'id_area_bach_est' : 'Area bachillerato *',
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
            'matri_est' : 'Matricula Estudiante*',
            'usuario_est' : 'Usuario*',
            'password_est' : 'Contraseña*',
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
    CTLD = (
        ('0','Seleccione una opción'),
        ('A','Aspirante'),
        ('E','Estudiante'),
        ('I','Ingenieria'),
        ('T','Titulado'),
    ) # 
    importante_doc = forms.ChoiceField(label='Importancia del Documento *', choices=DIFC, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estatus_grado = forms.ChoiceField(label='Categoria del Documento', choices=CTGDOC, widget=forms.Select(attrs={'class':'form-control', 'style':'border-color:#21B64A;'}))
    cve_control_doc = forms.ChoiceField(label='Clave de Control del Documento:*', choices=CTLD, widget=forms.Select(attrs={'class':'form-control', 'style':'border-color:#21B64A;'}))
    
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
        }
        labels ={
            'id_doc' : 'Clave del Documento *',
            'descri_largo_doc' : 'Nombre del Documento *',
            'descri_corto_doc' : 'Abreviatura del Documento *',
            'cve_control_doc' : 'Clave de Control del Documento *',
        }
##forms Grupo
class FormGrupo(forms.ModelForm):
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_grado = forms.ModelChoiceField(queryset = SeCatGrado.objects.filter(estatus_gra="A"),
                                  required=True,
                                  label="Grado: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatGrupo
        fields = '__all__'
        exclude = ('rowid_grupo','estatus_gpo',)
        widgets = {
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
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model= SeCatSalones
        fields= '__all__'
        exclude = ('rowid_salon', 'estatus_salon')
        widgets = {
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
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_col = forms.ModelChoiceField(queryset = SeCatColonia.objects.filter(estatus_col="A"),
                                  required=True,
                                  label="Colonia: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_academico = forms.ModelChoiceField(queryset = SeCatNivelAcademico.objects.filter(estatus_acade="A"),
                                  required=True,
                                  label="Nivel Academico: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_depto = forms.ModelChoiceField(queryset = SeCatDeptoEmp.objects.filter(estatus_depto="A"),
                                  required=True,
                                  label="Departamento: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_edo = forms.ModelChoiceField(queryset = SeCatEstado.objects.filter(estatus_edo="A"),
                                  required=True,
                                  label="Estado: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_sueldo = forms.ModelChoiceField(queryset = SeCatSueldos.objects.filter(estatus_sueldo="A"),
                                  required=True,
                                  label="Sueldo: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeCatEmpleado
        fields = '__all__'
        exclude = ('rowid_empleado', 'estatus_emp')
        widgets = { 
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
    rowid_plaza = forms.ModelChoiceField(queryset = SeCatPlaza.objects.filter(estatus_plaza="A"),
                                  required=True,
                                  label="Plaza: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model= SeCatTipoPuesto
        fields= '__all__'
        exclude = ('estatus_pue',)
        widgets = {
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
                'id_puesto':'ID del Puesto *',
                'descri_largo_pue':'Puesto *',
                'descri_corto_pue' : 'Abreviacion *',
        }
# Froms Sueldos
class FormSueldo(forms.ModelForm):
    rowid_puesto = forms.ModelChoiceField(queryset = SeCatTipoPuesto.objects.filter(estatus_pue="A"),
                                  required=True,
                                  label="Puesto: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model= SeCatSueldos
        fields= '__all__'
        exclude = ('rowid_sueldo','estatus_sueldo')
        widgets = {
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
            'clave_ser': forms.NumberInput(attrs={'class': 'form-control',
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
    rowid_institucion = forms.ModelChoiceField(queryset = SeCatInstitucion.objects.filter(estatus_ins="A"),
                                  required=True,
                                  label="Institucion: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_empleado = forms.ModelChoiceField(queryset = SeCatEmpleado.objects.filter(estatus_emp="A"),
                                  required=True,
                                  label="Empleado: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeTabEmpCar
        fields = '__all__'
        exclude = ('rowid_emp_car', 'estatus_inst')          
        widgets = {
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
            'descri_largo_car_emp': 'Carrera*',
            'descri_corto_car_emp': 'Abreviatura *',
        }

# -------------------------------------------- Operaciones --------------------------------------------- #

##########################  Operaciones #################################

# Froms Aspirantes
class FormsAspirantes(forms.ModelForm):
    SEXO = ( ('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Omitir') )
    EDOCIVIL = ( ('S', 'Soltero'), ('C','Casado'), ('V','Viudo'), ('D','Divorciado') )
    TRAB = ( ('S', 'Si'), ('N','No') )
    PERIODOS = ((0,'Seleccione el Periodo'),(1,'Enero-Abril'),(2,'Mayo-Agosto'),(3,'Septiembre-Diciembre'))
    TURNO = ( ('M','Matutino'), ('V','Vespertino') )
    DIS = ( ('S', 'Si'), ('N','No') )
    SERMED = ( ('S', 'Si'), ('N','No') )
    IND = ( ('S', 'Si'), ('N','No') )
    TIPSAN = (('No sé', 'No sé'),('AB+', 'AB+'),('O-', 'O-'),('O+', 'O+'),('A-', 'A-'),('A+', 'A+'),('B-', 'B-'),('B+', 'B+'),('AB-', 'AB-')) 
    sexo_asp = forms.ChoiceField(label='Sexo*', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    estado_civil_asp = forms.ChoiceField(label='Estado Civil', choices=EDOCIVIL, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    trabaja_asp = forms.ChoiceField(label='¿Trabaja?', choices=TRAB, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    periodo_asp = forms.ChoiceField(label='Periodo:*',choices=PERIODOS,widget=forms.Select(attrs={'class': 'form-control','style': 'border-color:#21B64A;'}))
    turno_asp = forms.ChoiceField(label='Turno*', choices=TURNO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    discapacidad = forms.ChoiceField(label='Discapacidad', choices=DIS, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    serviciomedico = forms.ChoiceField(label='Servicio Medico', choices=SERMED, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    indigena = forms.ChoiceField(label='Indigena', choices=IND, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    tipo_de_sangre_asp = forms.ChoiceField(label='Tipo de Sangre', choices=TIPSAN, widget=forms.Select(attrs={'class': 'form-control','required' : 'True','placeholder': 'Ingrese el tipo de sangre','style' : 'border-color:#21B64A;'}))
    rowid_mundel = forms.ModelChoiceField(queryset = SeCatMunicipioDelegacion.objects.filter(estatus_mundel="A"),
                                  required=True,
                                  label="Municipio/Alcaldía:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_area_bac = forms.ModelChoiceField(queryset = SeCatAreaBachillerato.objects.filter(estatus_bac="A"),
                                  required=True,
                                  label="Área Bachillerato:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_medio_dif = forms.ModelChoiceField(queryset = SeCatMedioDifusion.objects.filter(estatus_dif="A"),
                                  required=True,
                                  label="Medio de Difusión:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_esc_proc = forms.ModelChoiceField(queryset = SeCatEscuelaProcedencia.objects.filter(estatus_esc_proc="A"),
                                  required=True,
                                  label="Escuela de Procedencia: *",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_car = forms.ModelChoiceField(queryset = SeCatCarrera.objects.filter(estatus_car="A"),
                                  required=True,
                                  label="Carrera:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_col = forms.ModelChoiceField(queryset = SeCatColonia.objects.filter(estatus_col="A"),
                                  required=True,
                                  label="Colonia:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model= SeTabAspirante
        fields= '__all__'
        exclude = ('estatus_asp','rowid_asp','rowid_tipo_esc', 'fecha_alt_asp', 'user_alta', 'user_cambio')
        widgets = {
            'folio_utn_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el folio del aspirante',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),
            'calle_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese la calle',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'num_int_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Ingrese el número interior',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'num_ext_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el número exterior',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'codigo_postal_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el Código Postal',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'tel_cas_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el Teléfono',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'telefono_oficina_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Ingrese el Teléfono de Oficina',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'edad_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese la edad del aspirante',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'promedio_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el promedio',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'fecini_bach_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'DD/MM/AAAA',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'fecfin_bach_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'DD/MM/AAAA',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'rfc_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese su RFC',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'curp_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el CURP',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'fecha_nac_asp' : forms.DateInput(attrs={'class': 'form-control',
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
                                                    'placeholder': 'Ingrese el folio',
                                                    'style' : 'border-color:#21B64A;'
                                                    }),  
            'anio_asp' : forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese el año',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'mat_tutor_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el apellido materno del tutor',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'pat_tutor_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese el apellido paterno del tutor',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'nombre_tutor_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre del tutor',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'generacion_asp' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese la generación',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'email_asp' : forms.EmailInput(attrs={'class': 'form-control',
                                                'required' : 'True',
                                                'placeholder': 'Ingrese el Correo',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'opcioneducativa' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese la opción educativa',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'continuidadestudio' : forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Ingrese la continuidad de estudios',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'otromediodif' : forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Ingrese otro medio de difusión',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'otromedioinf' : forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Ingrese otro medio de información',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'otroopcioneduca' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese otra opción educativa',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'facebook' : forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese el Facebook',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'twitter' : forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingrese el Twitter',
                                                'style' : 'border-color:#21B64A;'
                                                }), 
            'tipodiscapacidad' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese el tipo de discapacidad',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'institucionseguro' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese la institución del seguro',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'otrainstitucionseguro' : forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Ingrese otra institución de seguro',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'numafiliacion' : forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Ingrese el número de afiliación',
                                                    'style' : 'border-color:#21B64A;'
                                                    }), 
            'fechaexpedicioncer' : forms.DateInput(attrs={'class': 'form-control',
                                                            'placeholder': 'DD/MM/AAAA',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'folio' : forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Ingrese el folio',
                                            'style' : 'border-color:#21B64A;'
                                            }), 
            'fechacompromisocerti' : forms.DateInput(attrs={'class': 'form-control',
                                                            'placeholder': 'DD/MM/AAAA',
                                                            'style' : 'border-color:#21B64A;'
                                                            }), 
            'poblacionindigena' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese la población indigena',
                                                        'style' : 'border-color:#21B64A;'
                                                        }), 
            'lenguaindigena' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese la lengua indigena que habla',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels = {
            'folio_utn_asp' : 'Folio del Aspirante*',
            'calle_asp' : 'Calle del Aspirante*' ,
            'num_int_asp' : 'Número Interior ' ,
            'num_ext_asp' : 'Número Exterior*',
            'codigo_postal_asp' : 'Código Postal*', 
            'tel_cas_asp' : 'Teléfono de Casa*', 
            'telefono_oficina_asp' : 'Teléfono de Oficina', 
            'edad_asp' : 'Edad*'  ,
            'promedio_asp' : 'Promedio del Aspirante*' ,
            'fecini_bach_asp' : 'Fecha de Inicio de Bachillerato*', 
            'fecfin_bach_asp' : 'Fecha de Termino de Bachillerato*',
            'rfc_asp' : 'RFC*' ,
            'curp_asp' : 'CURP*', 
            'fecha_nac_asp' : 'Fecha de Nacimiento*' ,
            'materno_asp' : 'Apellido Materno*' ,
            'paterno_asp' : 'Apellido Paterno*',
            'nombre_asp' : 'Nombre(s)*'  ,
            'folio_cen_asp' : 'Folio Cen del Aspirante', 
            'anio_asp' : 'Año del Aspirante',
            'mat_tutor_asp' : 'Apellido Materno*', 
            'pat_tutor_asp' : 'Apellido Paterno*' ,
            'nombre_tutor_asp' : 'Nombre(s)*',
            'generacion_asp' : 'Generación del Aspirante', 
            'email_asp' : 'Correo*' ,
            'opcioneducativa' : 'Opción Educativa', 
            'continuidadestudio' : 'Continuidad Estudio ', 
            'otromediodif' : 'Otro medio de Difusión ' ,
            'otromedioinf' : 'Otro medio de Información ', 
            'otroopcioneduca' : 'Otra opción Educativa ' ,
            'facebook' : 'Facebook' ,
            'twitter' : 'Twitter' ,
            'tipodiscapacidad' : 'Tipo de discapacidad'  ,
            'institucionseguro' : 'Institución de seguro del Aspirante', 
            'otrainstitucionseguro' : 'Otra Institución de Seguro' ,
            'numafiliacion' : 'Numero de afiliación' ,
            'fechaexpedicioncer' : 'Fecha de Expedición del Certificado ', 
            'folio' : 'Folio del Aspirante ' ,
            'fechacompromisocerti' : 'Fecha de Compromiso de Certificado', 
            'poblacionindigena' : 'Población Indigena ',
            'lenguaindigena' : 'Lengua Indigena ',
        }
# FORM documentos aspirante
class FormDocAsp(forms.ModelForm):
    RESPSN = (('','Seleccione una opción'), ('S', 'Si'), ('N','No')) # uno solo para los dos
    entrego_doc = forms.ChoiceField(label='¿Entrego?*', choices=RESPSN, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
    import_doc = forms.ChoiceField(label='¿Es Importante?*', choices=RESPSN, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))

    rowid_asp = forms.ModelChoiceField(queryset = SeTabAspirante.objects.filter(estatus_asp="A"),
                                  required=True,
                                  label="Aspirante:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_doc = forms.ModelChoiceField(queryset = SeCatDocumentacion.objects.filter(estatus_doc="A", cve_control_doc="A"),
                                  required=True,
                                  label="Documento:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeProAspDocu
        fields = '__all__'
        exclude = ('rowid_asp_docu', 'estatus_doc_aspi','fecha_alta_doc', 'fecha_cambio_doc', 'fecha_baja_doc', 'user_alta_doc', 'user_cambio_doc', 'user_baja_doc',)          
        widgets = {
            'comentario_doc': forms.Textarea(attrs={'class': 'form-control',
                                                    'required' : 'True',
                                                    'placeholder': 'Ingrese un comentario.',
                                                    'style' : 'border-color:#21B64A;'                                                        
                                                    }),
        }
        labels = {
            'comentario_doc': 'Comentario:*',
        }
# FORM documentos aspirante
class FormCalAsp(forms.ModelForm):
    rowid_asp = forms.ModelChoiceField(queryset = SeTabAspirante.objects.filter(estatus_asp="A"),
                                  required=True,
                                  label="Aspirante:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    rowid_indicador = forms.ModelChoiceField(queryset = SeCatIndicador.objects.filter(estatus_ind="A", cve_control_ind="A"),
                                  required=True,
                                  label="Indicador:*",
                                  widget=forms.Select(
                                      attrs={
                                        'onchange': 'load_sub_codes();',
                                        'class': 'form-control',
                                        'required' : 'True',
                                        'style' : 'border-color:#21B64A;'
                                      }
                                  )
                                  )
    class Meta:
        model = SeTabAceptados
        fields = '__all__'
        exclude = ('rowid_ace','estatus_ace')          
        widgets = {
            'calificacion_ace': forms.NumberInput(attrs={'class': 'form-control',
                                'required' : 'True',
                                'placeholder': 'Ingrese la calificacion.',
                                'style' : 'border-color:#21B64A;'                                                        
                                }),
            'folio_cen_ace': forms.TextInput(attrs={'class': 'form-control',
                                'required' : 'True',
                                'placeholder': 'Ingrese la calificacion.',
                                'style' : 'border-color:#21B64A;'                                                        
                                }),
        }
        labels = {
            'calificacion_ace': 'Calificaciones:*',
            'folio_cen_ace': 'Folio:*',
        }
