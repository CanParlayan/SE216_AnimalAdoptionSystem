from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock

Window.size = (370, 600)

screen_helper = '''
ScreenManager:
    SplashScreen:
    BulletinScreen:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    ForgotPassScreen:
    FollowedScreen:
    SubmitScreen:
    SupportScreen:
    AnimalPage1:
    AnimalPage2:
<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        password: True
        icon_left: "key-variant"

    MDIconButton:
        icon: 'camera'
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "camera" if self.icon == "camera" else "camera"
            text_field.password = False if text_field.password is True else True    
<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:''
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:'Animal Adoption'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.7}
    MDLabel:
        text:'System'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.5}
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.4,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.6,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Welcome To The Animal Adoption System !'
        font_style:'H4'
        halign:'center'
        pos_hint: {'center_y':0.8}
    MDTextField:

        id:userName
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username:'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password:'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'lock'
        icon_right_color: app.theme_cls.primary_color
        required: True
        password: True
        password_mask: '•'
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.2,0.1)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()

    MDTextButton:
        text: 'Dont have an account? Create one !'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
    MDTextButton:
        text:'Forgot Password?'
        pos_hint:{'center_x':0.5,'center_y':0.05}
        on_press:
            root.manager.current = 'forgotpassword'
            root.manager.transition.direction='up'        
<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Sign up to the Animal Adoption System!'
        font_style:'H4'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email:'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username:'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account-box'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.3,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password:'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'lock'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_ssn
        pos_hint: {'center_y':0.45,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Social Security Number:'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'smart-card'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account?'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'

<ForgotPassScreen>:
    name: 'forgotpassword'
    MDLabel:
        text:'We can help you remember!'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.8}
    MDLabel:
        text:'Please enter your email-address so we can contact you and get you a new password!'
        halign:'center'
        pos_hint: {'center_y':0.5}
    MDTextField:
        id:userName
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'E-mail address:'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Reset'
        size_hint: (0.2,0.1)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            root.manager.current='loginscreen'
            root.manager.transition.direction='down'
            app.forgotPassword()




<FollowedScreen>
    name: 'followedscreen'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                id: screen1
                BoxLayout:
                    id: layout
                    orientation: 'vertical'     
                    MDToolbar:
                        id: main_toolbar
                        title: 'Followed Posts'
                        headline_text : 'Hello'
                        anchor_title : 'left'
                        left_action_items: [["paw", lambda x : nav_drawer.set_state("open")],["arrow-left",lambda x: app.navToBulletin()]]
                        elevation:5
                    MDGridLayout:
                        cols: 2
                        row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                        row_force_default: False
                        adaptive_height: False
                        padding: dp(4), dp(4)
                        spacing: dp(4)
                        SmartTileWithLabel:
                            text:   '  '
                            source: "img/dog1.jpg"
                        MDLabel:
                            text: "My French Bulldog has disappeared. It is collarless. The area around his two eyes is black and white."                        

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "5dp"
                spacing: "5dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "img/logo.png"

                MDLabel:
                    text: ""
                    font_style: "Subtitle1"
                    size_hint_y: None
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    height: self.texture_size[1]

                ScrollView:

                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Ecem Konca"

                                IconLeftWidget:
                                    icon: "face-woman"



                            OneLineIconListItem:
                                text: "Halil Can Parlayan"

                                IconLeftWidget:
                                    icon: "face"


                            OneLineIconListItem:
                                text: "Hamza Çekirdek"

                                IconLeftWidget:
                                    icon:"face"        

<SubmitScreen>
    name: 'submitscreen'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    id: screen1
                    BoxLayout:
                        id: layout
                        orientation: 'vertical'     
                        MDToolbar:
                            id: main_toolbar
                            title: 'Create an announcement'
                            headline_text : 'Hello'
                            anchor_title : 'center'
                            left_action_items: [["paw", lambda x : nav_drawer.set_state("open")],["arrow-left",lambda x: app.navToBulletin()]]
                            elevation:5
                        MDTextField:
                            id : empty
                            helper_text_mode: "on_focus"
                            size_hint_x:None 
                            width: 5     
                        MDFloatLayout:

                            MDRoundFlatIconButton:
                                text: "Choose a photo"
                                icon: "folder"
                                pos_hint: {'center_x': .5, 'center_y': .6}
                                on_release: app.null()    
                        MDTextField:
                            id: breed
                            hint_text: "Breed"
                            helper_text: "Please enter the breed of the animal"
                            helper_text_mode: "on_focus"
                            icon_right: "paw"
                            icon_right_color: app.theme_cls.primary_color
                            pos_hint:{'center_x': 0.5, 'center_y': 0.63}
                            size_hint_x:None
                            width: 300                                                                                            
                        MDTextField:
                            id: age
                            hint_text: "Age of the animal"
                            helper_text: "Please only enter numerical inputs"
                            helper_text_mode: "on_focus"
                            icon_right: "paw"
                            icon_right_color: app.theme_cls.primary_color
                            pos_hint:{'center_x': 0.5, 'center_y': 0.55}
                            size_hint_x:None
                            width:300 
                        MDTextField:
                            id: phone
                            hint_text: "Phone number"
                            helper_text: "Please enter your phone number"
                            helper_text_mode: "on_focus"
                            icon_right: "paw"
                            icon_right_color: app.theme_cls.primary_color
                            pos_hint:{'center_x': 0.5, 'center_y': 0.47}
                            size_hint_x:None
                            width:300 
                        MDTextField:
                            id: address
                            hint_text: "Address"
                            helper_text: "Your address so we can pick up the animal"
                            helper_text_mode: "on_focus"
                            icon_right: "paw"
                            icon_right_color: app.theme_cls.primary_color
                            pos_hint:{'center_x': 0.5, 'center_y': 0.39}
                            size_hint_x:None
                            width:300 
                        MDTextField:
                            id: mail
                            hint_text: "Mail address"
                            helper_text: "Please enter your mail address"
                            helper_text_mode: "on_focus"
                            icon_right: "paw"
                            icon_right_color: app.theme_cls.primary_color
                            pos_hint:{'center_x': 0.5, 'center_y': 0.31}
                            size_hint_x:None
                            width:300 
                        MDTextField:
                            id: details
                            hint_text: "More Details"
                            helper_text: "You can give out more details if you want"
                            helper_text_mode: "on_focus"
                            icon_right: "paw"
                            multiline: True
                            icon_right_color: app.theme_cls.primary_color
                            pos_hint:{'center_x': 0.5, 'center_y': 0.23}
                            size_hint_x:None
                            max_text_length: 250
                            width:300                          

                        MDBottomAppBar:
                            MDToolbar:
                                icon: 'check'
                                text: 'hello'
                                type: 'bottom'
                                on_action_button: app.submission()
                                mode: "center"               

                        Widget:

            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
                    orientation: 'vertical'
                    padding: "5dp"
                    spacing: "5dp"

                    Image:
                        id: avatar
                        size_hint: (1,1)
                        source: "img/logo.png"

                    MDLabel:
                        text: ""
                        font_style: "Subtitle1"
                        size_hint_y: None
                        halign: "center"
                        valign: "center"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        height: self.texture_size[1]

                    ScrollView:

                        DrawerList:
                            id: md_list

                            MDList:
                                OneLineIconListItem:
                                    text: "Ecem Konca"

                                    IconLeftWidget:
                                        icon: "face-woman"



                                OneLineIconListItem:
                                    text: "Halil Can Parlayan"

                                    IconLeftWidget:
                                        icon: "face"


                                OneLineIconListItem:
                                    text: "Hamza Çekirdek"

                                    IconLeftWidget:
                                        icon : "face"

<SupportScreen>
    name: 'supportscreen'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                id: screen1
                BoxLayout:
                    id: layout
                    orientation: 'vertical'     
                    MDToolbar:
                        id: main_toolbar
                        title: 'Support'
                        headline_text : ''
                        anchor_title : 'left'
                        left_action_items: [["paw", lambda x : nav_drawer.set_state("open")],["arrow-left",lambda x: app.navToBulletin()]]
                        elevation:5
                    MDLabel:
                        text: "You can inform us about your opinions, suggestions or problems you experience while using the program."
                        halign : 'center'             
                    MDTextField:
                        size_hint_x: .5
                        hint_text: ""
                        max_height: "200dp"
                        mode: "fill"
                        fill_color: 0, 0, 0, .4
                        multiline: True
                        pos_hint: {"center_x": .5, "center_y": 2}
                        max_text_length: 500

                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'check'
                            text: 'hello'
                            type: 'bottom'
                            on_action_button: app.supportTicket()
                            mode: "center"               

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "5dp"
                spacing: "5dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "img/logo.png"

                MDLabel:
                    text: ""
                    font_style: "Subtitle1"
                    size_hint_y: None
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    height: self.texture_size[1]

                ScrollView:

                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Ecem Konca"

                                IconLeftWidget:
                                    icon: "face-woman"



                            OneLineIconListItem:
                                text: "Halil Can Parlayan"

                                IconLeftWidget:
                                    icon: "face"


                            OneLineIconListItem:
                                text: "Hamza Çekirdek"

                                IconLeftWidget:
                                    icon:"face" 

<BulletinScreen>
    name: 'bulletinscreen'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                id: screen1
                BoxLayout:
                    id: layout
                    orientation: 'vertical'     
                    MDToolbar:
                        id: main_toolbar
                        title: 'Bulletin'
                        headline_text : 'Hello'
                        anchor_title : 'center'
                        left_action_items: [["paw", lambda x : nav_drawer.set_state("open")]]
                        right_action_items: [["human-greeting", lambda x: app.navToProfile()]]
                        elevation:5
                    MDGridLayout:
                        cols: 2
                        row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
                        row_force_default: False
                        adaptive_height: False
                        padding: dp(4), dp(4)
                        spacing: dp(4)
                        SmartTileWithLabel:
                            text:   '  '
                            source: "img/dog1.jpg"
                            on_press: app.navToAnimalPage1()
                        MDLabel:
                            text: "My French Bulldog has disappeared. It is collarless. The area around his two eyes is black and white."
                        SmartTileWithLabel:
                            text:   '  '
                            source: "img/cat.jpeg"
                            on_press: app.navToAnimalPage2()
                        MDLabel:
                            text: "Our cat has disappeared today. There is a reward for finding"    
                        SmartTileWithLabel:
                            source: "img/dog2.jpeg"
                            text:   '  '
                        MDLabel:
                            text: "We found a white terrier living on the street in Ankara Bağlıca. The dog is around 1.5 years old. We want to give it to a clean, good-natured person."     
                        SmartTileWithLabel:
                            text: "Tangerines\\n[size=12]tangerines-1111529_1280.jpg[/size]"
                            source: "img/dog1.jpg"
                        MDLabel:
                            text: "Robin\\n[size=12]robin-944887_1280.jpg[/size]"          


                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'plus'
                            text: 'hello'
                            type: 'bottom'
                            left_action_items: [["heart", lambda x: app.navToFollowed()]]
                            right_action_items:[["help", lambda x: app.navToSupport(), "Support"]]
                            on_action_button: app.navToSubmit()
                            mode: "center"               

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "5dp"
                spacing: "5dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "img/logo.png"

                MDLabel:
                    text: ""
                    font_style: "Subtitle1"
                    size_hint_y: None
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    height: self.texture_size[1]

                ScrollView:

                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Ecem Konca"

                                IconLeftWidget:
                                    icon: "face-woman"



                            OneLineIconListItem:
                                text: "Halil Can Parlayan"

                                IconLeftWidget:
                                    icon: "face"


                            OneLineIconListItem:
                                text: "Hamza Çekirdek"

                                IconLeftWidget:
                                    icon:"face"
<SplashScreen>
 
    name: "splashscreen"
    on_enter: self.ids.progress.start()
    MDBoxLayout:
        md_bg_color: rgba(255, 255, 255)
        MDFloatLayout:
            Image:
                source:'img/loading.png'
                allow_stretch: True
                anim_delay: 1
                pos_hint:{'center_y':.7, 'center_x':.5}

            BoxLayout:
                pos_hint:{'center_y':.3, 'center_x':.5}
                padding: "10dp"
                size_hint_x: .7
                
                Image:
                    source:'img/load.gif'
                    allow_stretch: False
                    anim_delay: 0.2
                    anim_loop: 30
                    anim_reset: False
                    pos_hint:{'center_y':.4, 'center_x':.5}                                  
<AnimalPage1>
    name: 'animalpage1'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                id: screen1
                BoxLayout:
                    id: layout
                    orientation: 'vertical'     
                    MDToolbar:
                        id: main_toolbar
                        title: 'Animal Page 1'
                        headline_text : 'Hello'
                        anchor_title : 'left'
                        left_action_items: [["paw", lambda x : nav_drawer.set_state("open")],["arrow-left",lambda x: app.navToBulletin()]]
                        right_action_items: [["heart-outline"]]
                        elevation:5
                    BoxLayout:
                        id: layout1
                        size_hint_y: None 
                        height: dp(400)
                        orientation: 'vertical'
                    
                        MDLabel:                                       
                            text: 'Lost : French Bulldog'             
                            font_style: "H3"                    
                            size_hint_y: None                          
                            halign: "center"                           
                            valign: "center"                           
                            pos_hint: {"center_x": .5, "center_y": .9} 
                        
                        Image:
                            source: 'img/dog1.jpg'
                            size: self.size
                        
                        MDLabel:                                       
                            text: 'My French Bulldog has disappeared. It is collarless. The area around his two eyes is black and white.'             
                            font_style: "H6"                    
                            size_hint_y: None                          
                            halign: "center"                           
                            valign: "center"                           
                            pos_hint: {"center_x": .5, "center_y": .2}
                        MDFillRoundFlatIconButton:
                            icon: "phone"
                            text: "+905893487382"
                            halign: "center"
                            valign: "center"
                            pos_hint: {"center_x": .5, "center_y": .2}        
         
                    
                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'heart'
                            text: 'hello'
                            type: 'bottom'
                            on_action_button: app.favorite()
                            mode: "center"               

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "5dp"
                spacing: "5dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "img/logo.png"

                MDLabel:
                    text: ""
                    font_style: "Subtitle1"
                    size_hint_y: None
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    height: self.texture_size[1]

                ScrollView:

                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Ecem Konca"

                                IconLeftWidget:
                                    icon: "face-woman"



                            OneLineIconListItem:
                                text: "Halil Can Parlayan"

                                IconLeftWidget:
                                    icon: "face"


                            OneLineIconListItem:
                                text: "Hamza Çekirdek"

                                IconLeftWidget:
                                    icon:"face"
<AnimalPage2>
    name: 'animalpage2'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                id: screen1
                BoxLayout:
                    id: layout
                    orientation: 'vertical'     
                    MDToolbar:
                        id: main_toolbar
                        title: 'Animal Page 2'
                        headline_text : 'Hello'
                        anchor_title : 'left'
                        left_action_items: [["paw", lambda x : nav_drawer.set_state("open")],["arrow-left",lambda x: app.navToBulletin()]]
                        right_action_items: [["heart"]]
                        elevation:5         
                    BoxLayout:
                        id: layout1
                        size_hint_y: None 
                        height: dp(400)
                        orientation: 'vertical'
                    
                        MDLabel:                                       
                            text: 'Stray Animal : White Terrier'             
                            font_style: "H3"                    
                            size_hint_y: None                          
                            halign: "center"                           
                            valign: "center"                           
                            pos_hint: {"center_x": .5, "center_y": .9} 
                        
                        Image:
                            source: 'img/dog2.jpeg'
                            size: self.size
                        
                        MDLabel:                                       
                            text: 'We found a white terrier living on the street in Ankara Bağlıca. The dog is around 1.5 years old. We want to give it to a clean, good-natured person.'             
                            font_style: "H6"                    
                            size_hint_y: None                          
                            halign: "center"                           
                            valign: "center"                           
                            pos_hint: {"center_x": .5, "center_y": .2}
                        MDFillRoundFlatIconButton:
                            icon: "phone"
                            text: "+905427891245"
                            halign: "center"
                            valign: "center"
                            pos_hint: {"center_x": .5, "center_y": .2}

                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'heart'
                            text: 'hello'
                            type: 'bottom'
                            on_action_button: app.favorite()
                            mode: "center"               

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "5dp"
                spacing: "5dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "img/logo.png"

                MDLabel:
                    text: ""
                    font_style: "Subtitle1"
                    size_hint_y: None
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    height: self.texture_size[1]

                ScrollView:

                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Ecem Konca"

                                IconLeftWidget:
                                    icon: "face-woman"



                            OneLineIconListItem:
                                text: "Halil Can Parlayan"

                                IconLeftWidget:
                                    icon: "face"


                            OneLineIconListItem:
                                text: "Hamza Çekirdek"

                                IconLeftWidget:
                                    icon:"face"                                                                              
'''


class WelcomeScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class ForgotPassScreen(Screen):
    pass


class BulletinScreen(Screen):
    pass


class SubmitScreen(Screen):
    pass


class SupportScreen(Screen):
    pass


class FollowedScreen(Screen):
    pass


class AnimalPage1(Screen):
    pass


class AnimalPage2(Screen):
    pass
class SplashScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='loginscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(ForgotPassScreen(name='forgotpassword'))
sm.add_widget(BulletinScreen(name='bulletinscreen'))
sm.add_widget(SubmitScreen(name='submitscreen'))
sm.add_widget(SupportScreen(name='supportscreen'))
sm.add_widget(FollowedScreen(name='followedscreen'))
sm.add_widget(AnimalPage1(name='animalpage1'))
sm.add_widget(AnimalPage2(name='animalpage2'))
sm.add_widget(SplashScreen(name='splashscreen'))


class AnimalAdoptionSystem(MDApp):
    class ClickableTextFieldRound(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def navToSubmit(self):
        self.strng.get_screen('bulletinscreen').manager.current = 'submitscreen'

    def navToBulletin(self):
        self.strng.get_screen('bulletinscreen').manager.current = 'bulletinscreen'

    def navToAnimalPage1(self):
        self.strng.get_screen('bulletinscreen').manager.current = 'animalpage1'

    def navToAnimalPage2(self):
        self.strng.get_screen('bulletinscreen').manager.current = 'animalpage2'

    def supportTicket(self):
        Snackbar(

            text="Your ticket is received.",
            snackbar_x="10dp",
            snackbar_y="10dp",
        ).open()
        self.strng.get_screen('supportscreen').manager.current = 'bulletinscreen'

    def submission(self):
        self.strng.get_screen('submitscreen').manager.current = 'bulletinscreen'
        Snackbar(
            text="Your submission is now awaiting confirmation!",
            snackbar_x="10dp",
            snackbar_y="40dp",
        ).open()

    def navToSupport(self):
        self.strng.get_screen('supportscreen').manager.current = 'supportscreen'

    def navToProfile(self):
        self.strng.get_screen('bulletinscreen').manager.current = 'welcomescreen'

    def navToFollowed(self):
        self.strng.get_screen('bulletinscreen').manager.current = 'followedscreen'

    def forgotPassword(self):
        Snackbar(
            text="Please click the link on your inbox",
            snackbar_x="10dp",
            snackbar_y="40dp",
        ).open()
    def null(self):
        print("Null")

    def favorite(self):
        Snackbar(
            text="The page is added to favorites.",
            snackbar_x="10dp",
            snackbar_y="40dp",
        ).open()
        self.strng.get_screen('followedscreen').manager.current = 'bulletinscreen'

    def on_start(self):
        Clock.schedule_once(self.change_screen, 7)

    def build(self):
        self.icon = 'img/icon.ico'
        self.title = "Animal Adoption System"
        self.theme_cls.primary_palette = "Red"
        self.strng = Builder.load_string(screen_helper)
        return self.strng
    def change_screen(self, dt):
        self.strng.get_screen('splashscreen').manager.current = 'bulletinscreen'

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        signupSSN = self.strng.get_screen('signupscreen').ids.signup_ssn.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == [] \
                or signupSSN.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'



    def login(self):
        userName = self.strng.get_screen('loginscreen').ids.userName.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        if userName == "CanPar" and loginPassword == "can":
            self.login_check = True
            self.strng.get_screen('loginscreen').manager.current = 'bulletinscreen'
            Snackbar(
                text="Welcome " + userName,
                snackbar_x="10dp",
                snackbar_y="40dp",
            ).open()
        else:
            Snackbar(
                text="Wrong password or username combination!",
                snackbar_x="10dp",
                snackbar_y="40dp",
            ).open()

    def close_username_dialog(self, obj):
        self.dialog.dismiss()



AnimalAdoptionSystem().run()
