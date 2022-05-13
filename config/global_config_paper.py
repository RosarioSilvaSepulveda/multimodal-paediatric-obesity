import matplotlib.colors
import seaborn as sns

# Color palette
blue_rgb       = (78/255,  121/255, 167/255)
orange_rgb     = (242/255, 142/255, 43/255)
red_rgb        = (225/255, 87/255,  89/255)
turquoise_rgb  = (118/255, 183/255, 178/255)
green_rgb      = (89/255,  161/255, 79/255)
yellow_rgb     = (237/255, 201/255, 72/255)
purple_rgb     = (176/255, 122/255, 161/255)
pink_rgb       = (255/255, 157/255, 167/255)
brown_rgb      = (156/255, 117/255, 95/255)
gray_rgb       = (186/255, 176/255, 172/255)

sns_saturation = 1

palette_def = [blue_rgb,
               orange_rgb,
               red_rgb,
               turquoise_rgb,
               green_rgb,
               yellow_rgb,
               purple_rgb,
               pink_rgb,
               brown_rgb,
               gray_rgb]

# Blues (2 shades)
blue_shades = [(78/255,  121/255, 167/255),
               (163/255, 201/255, 220/255)]

# More color definitions
conf_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(255/255,255/255,215/255), turquoise_rgb, blue_rgb])
pos_cmap =  matplotlib.colors.LinearSegmentedColormap.from_list("", [(205/255,242/255,246/255),(23/255,39/255,82/255)])
neg_pos_cmap =  matplotlib.colors.LinearSegmentedColormap.from_list("", [blue_rgb,orange_rgb])

# Style definitions
sns.set_style({'axes.facecolor': 'white',
               'axes.edgecolor': '.8',
               'axes.grid': True,
               'axes.axisbelow': True,
               'axes.labelcolor': '.15',
               'figure.facecolor': 'white',
               'grid.color': '.8',
               'grid.linestyle': '-',
               'text.color': '.15',
               'xtick.color': '.15',
               'ytick.color': '.15',
               'xtick.direction': 'out',
               'ytick.direction': 'out',
               'lines.solid_capstyle': 'round',
               'patch.edgecolor': 'w',
               'image.cmap': 'rocket',
               'font.family': ['sans-serif'],
               'font.sans-serif': ['Arial',
               'DejaVu Sans',
               'Liberation Sans',
               'Bitstream Vera Sans',
               'sans-serif'],
               'patch.force_edgecolor': False,
               'xtick.bottom': False,
               'xtick.top': False,
               'ytick.left': False,
               'ytick.right': False,
               'axes.spines.left': False,
               'axes.spines.bottom': True,
               'axes.spines.right': False,
               'axes.spines.top': False}
)
matplotlib.rcParams.update({'font.size': 15})


# Funtion for showing data labels as percentages
def show_label_percent(df):
    for ax in df.axes.ravel():
        
        # add annotations
        for c in ax.containers:
        
            # custom label calculates percent and add an empty string so 0 value bars don't have a number
            labels = [f'{w:0.1f}%' if (w := v.get_height()) > 0 else '' for v in c]
    
            ax.bar_label(c, labels=labels, label_type='edge', fontsize=16, rotation=0, padding=2)
        
        ax.margins(y=0.2)
        
        
# Funtion for showing data labels as quantities
def show_label_quantity(df):
    for ax in df.axes.ravel():
        
        # add annotations
        for c in ax.containers:
        
            # custom label calculates percent and add an empty string so 0 value bars don't have a number
            labels = [f'{w:0.1f}' if (w := v.get_height()) > 0 else '' for v in c]
    
            ax.bar_label(c, labels=labels, label_type='edge', fontsize=16, rotation=0, padding=2)
        
        ax.margins(y=0.2)

# Seed
seed = 27

# Number of folder CV
n_folds = 5

# Mapping emotions
emotion_id_to_emotion = {'adm':'admiration',
                         'amu':'amusement',
                         'att':'tenderness',
                         'col':'anger',
                         'deg':'disgust',
                         'des':'despair',
                         'fie':'pride',
                         'hon':'shame',
                         'inq':'anxiety',
                         'int':'interest',
                         'irr':'irritation',
                         'joi':'joy',
                         'mep':'contempt',
                         'peu':'panic',
                         'pla':'pleasure',
                         'sou':'relief',
                         'sur':'surprise',
                         'tri':'sadness'
                        }
emotion_to_emotion_id = dict(zip(emotion_id_to_emotion.values(), emotion_id_to_emotion.keys()))

emotion_fr_id_to_emotion_eng_id = {'adm':'adm',
                                   'amu':'amu',
                                   'att':'ten',
                                   'col':'ang',
                                   'deg':'dis',
                                   'des':'des',
                                   'fie':'pri',
                                   'hon':'sha',
                                   'inq':'anx',
                                   'int':'int',
                                   'irr':'irr',
                                   'joi':'joy',
                                   'mep':'con',
                                   'peu':'fea',
                                   'pla':'ple',
                                   'sou':'rel',
                                   'sur':'sur',
                                   'tri':'sad'
                                  }
emotion_eng_id_to_emotion_fr_id = dict(zip(emotion_fr_id_to_emotion_eng_id.values(), emotion_fr_id_to_emotion_eng_id.keys()))

#emotion_eng_id_to_emotion_num
label_id_to_label_num = {"Normal":0,
                         "Overweight or Obese":1}

label_id_to_label ={0: "Normal",
                    1: "Overweight or Obese"}

label_id_to_short_label ={0: "Norm",
                    1: "OwOb"}

sex_id_to_sex = {1:"male",
                 2:"female"}

region_id_to_region = {1: "North",
                       2: "Centre",
                       3: "Mexico_City",
                       4: "South"}

strata_id_to_strata = {1: "1st_strata",
                       2: "2nd_strata",
                       3: "3rd_strata",
                       4: "4th_strata"}

locality_size_id_to_locality_size = {1:"more_100k",
                                     2: "15_99k",
                                     3: "2.5_14k",
                                     4: "less_2.5k"}

locality_type_id_to_locality_type = {1: "urban",
                                     2: "rural"}

label_id_to_label_num_coef_int = {"Overweight or Obese":1}

label_id_to_label_id = {"Normal":"Normal",
                        "Overweight or Obese":"Overweight or Obese"}

emotion_eng_id_to_emotion_num = {'adm':0,
                                 'amu':1,
                                 'ten':2,
                                 'ang':3,
                                 'dis':4,
                                 'des':5,
                                 'pri':6,
                                 'sha':7,
                                 'anx':8,
                                 'int':9,
                                 'irr':10,
                                 'joy':11,
                                 'con':12,
                                 'fea':13,
                                 'ple':14,
                                 'rel':15,
                                 'sur':16,
                                 'sad':17
                                }

#emotion_num_to_emotion_id
label_num_to_label_id = dict(zip(label_id_to_label_num.values(), label_id_to_label_num.keys()))


emotion_num_to_emotion_eng_id = dict(zip(label_id_to_label_num.values(), label_id_to_label_num.keys()))

emotion_id_to_valence = {'adm':'pos',
                         'amu':'pos',
                         'att':'pos',
                         'col':'neg',
                         'deg':'neg',
                         'des':'neg',
                         'fie':'pos',
                         'hon':'neg',
                         'inq':'neg',
                         'int':'pos',
                         'irr':'neg',
                         'joi':'pos',
                         'mep':'neg',
                         'peu':'neg',
                         'pla':'pos',
                         'sou':'pos',
                         'sur':'pos',
                         'tri':'neg'
                         }


# Mapping actor_id to sex
actor_id_to_sex = {1:'m',
                   2:'f',
                   3:'m',
                   4:'m',
                   5:'m',
                   6:'f',
                   7:'f',
                   8:'m',
                   9:'f',
                   10:'f',
                   }
