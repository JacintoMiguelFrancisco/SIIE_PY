import string
from django import forms

from .models import (SeCatPais, SeCatEstado, SeCatMunicipioDelegacion,SeCatColonia,  # Direcciones
                    SeCatUniversidad, SeCatDivision, SeCatCarrera, SeCatPeriodos, # Universidades
                    SeCatMedioDifusion, SeCatTipoEscuela, SeCatAreaBachillerato, SeProIndAsp, # Aspirantes
                    SeCatGrado, SeCatSalones, SeCatTipoBajas, SeCatBecas, SeCatTipoCambio, # Estudintes
                    SeCatEmpleado, SeCatNivelAcademico, SeCatPlaza, SeCatTipoPuesto, SeCatSueldos, SeCatDeptoEmp, SeCatActividades, SeCatInstitucion, SeTabEmpCar, # Empleados
                    SeCatIndicador, SeCatPlaEstudio, SeTabAspirante
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

# -------------------------------------------- Aspirantes --------------------------------------------- #

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
    # SEXO =( ('M', 'Masculino'), ('F', 'Femenino') )
    # sexo_emp = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control', 'style' : 'border-color:#21B64A;'}))
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
            'sexo_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el sexo del empleado', 
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
            'estatus_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el estatus del empleado', 
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
            'estatus_val': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el estatus', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'estatus_comp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el estatus', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'edad_emp': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese la edad del empleado', 
                                                        'style' : 'border-color:#21B64A;', 
                                                        'required' : 'True'
                                                      }), 
            'estado_civil_emp': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el estado civil del empleado', 
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
            'tipo_contrato_com': forms.NumberInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el tipo de contrato del empleado', 
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
            'estatus_biblio': forms.TextInput(attrs={'class': 'form-control', 
                                                        'placeholder': 'Por favor, Ingrese el estatus', 
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
                'sexo_emp':'Sexo',
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
                'estatus_val':'Estatus Val',
                'estatus_comp':'Estatus Comp',
        #         'estatus_val':'estos estatus son dependiendo los roles',(Rh y division) 
        #         'estatus_comp':'S', 
                'edad_emp':'Edad', 
                'estado_civil_emp':'Estado Civil',
                'num_vac_max':'Numero Maximo de Vacaciones',
                'num_vac_act':'Numero de Vacaciones Actuales',
                'tipo_contrato_com' : 'Tipo de Contrato',
        #         'num_vac_max':'numero de vacaciones', 
        #         'num_vac_act':'actuales', 
        #         'tipo_contrato_com':'1, permante, 2 temporal',
                'cedula_emp_com':'Cedula Profesional', 
                'fecicon':'Fecha de Inicio de Contrato',
                'fecfcon':'Fecha Final de Contrato',
        #         'fecicon':'inicio', 
        #         'fecfcon':'fin contrato', 
                'comentario_emp':'Comentario',
                'estatus_biblio':'Estatus Biblioteca', 
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











#Form INDICADORES 
class FormsIndicador(forms.ModelForm):
    class Meta:
        model= SeCatIndicador
        fields= '__all__'
        exclude = ('id_indicador', 'estatus_ind')
        widgets = {
            'descri_largo_ind' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese el nombre del indicador.',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),

            'descri_corto_ind' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la abreviatura',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),

            'cve_control_ind' : forms.TextInput(attrs={'class': 'form-control',
                                                        'required' : 'True',
                                                        'placeholder': 'Ingrese la clave de control',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),
        }
        labels ={
                'descri_largo_ind' : 'Nombre *',
                'descri_corto_ind' : 'Abreviatura *',
                'cve_control_ind' : 'Clave *',
        }
# Form PLAN DE ESTUDIO 
class FormsPlaE(forms.ModelForm):
    class Meta:
        model= SeCatPlaEstudio
        fields = '__all__'
        exclude = ('id_plan_est', 'estatus_plan_est')
        widgets = {
            'decri_larga_plan_est' : forms.TextInput(attrs={'class': 'form-control',
                                                            'required' : 'True',
                                                            'placeholder': 'Ingrese el nombre del plan',
                                                            'style' : 'border-color:#21B64A;'
                                                            }),

            'descri_corta_plan_est' : forms.TextInput(attrs={'class': 'form-control',
                                                                'required' : 'True',
                                                                'placeholder': 'Ingrese la abreviatura',
                                                                'style' : 'border-color:#21B64A;'
                                                                }),

            'fec_alta_estpla' : forms.DateInput(attrs={'class': 'form-control',
                                                        'placeholder': 'DD/MM/AAAA',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),

            'user_alta_estpla' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese el usuario que modificó:',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),

            'fec_baja_estpla' :  forms.DateInput(attrs={'class': 'form-control',
                                                        'placeholder': 'DD/MM/AAAA',
                                                        'style' : 'border-color:#21B64A;'
                                                        }),

            'user_baja_estpla' : forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingrese el usuario que modificó:', 
                                                        'style' : 'border-color:#21B64A;'
                                                        })
        }
        ###cambiar data tiem por la otra madre
        labels ={
                'decri_larga_plan_est' : 'Nombre *',
                'descri_corta_plan_est' : 'Abreviatura *',
                'fec_alta_estpla' : 'Fecha de alta',
                'user_alta_estpla' : 'Usuario',
                'fec_baja_estpla' : 'Fecha de baja',
                'user_baja_estpla' :'Usuario',
        }



# -------------------------------------------- Operaciones --------------------------------------------- #

##########################  Operaciones #################################
# Froms Aspirantes
class FormsAspirantes(forms.ModelForm):
    class Meta:
        model= SeTabAspirante
        fields= '__all__'
        # exclude = ('id_uni','id_div','id_car')
        widgets = {
            # 'descri_corto_gra' : forms.TextInput(attrs={'class': 'form-control',
            #                                             'required' : 'True',
            #                                             'placeholder': 'Ingrese el grado.',
            #                                             'style' : 'border-color:#21B64A;'
            #                                             }),
        }

        labels = {

                # 'descri_corto_gra' : 'Grado *',
        }

    # id_uni / id_div / id_car /  descri_largo_car / descri_corto_car   /  estatus_car / ceneval_car / descri_largo_tit