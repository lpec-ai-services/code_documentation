<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/src_dir.html -->

# The src directory

The `src` directory contains all source files required to build CORBA engine and (optionally) GUI libraries of the module. Each of these entities usually has (but this is not actually obligatory) its own directory.

The `CMakeLists.txt` file triggers the path of sub-directories described by the *ADD_SUBDIRECTORY()* command.

- `src/HELLO` sub-directory

This sub-directory contains the C++ source files that implement the engine library of the module. The `CMakeLists.txt` defines the rules used to build the engine library from these source files. The name of the module engine library is predefined and should be set as `lib<MODULE>Engine.so` where `MODULE` is a name of the module. In the case of the HELLO module, the name of the engine library should be `libHELLOEngine.so`.

The `HELLO.h`, `HELLO.cxx` files implement *HELLO* class that is derived from the *HELLO_Gen* interface of the *HELLO_ORB__POA* CORBA module and the *SALOME_Component_i* class (base implementation of SALOME module engine exported by the KERNEL module).

In particular, *HELLO* class implements *hello()* and *goodbye()* functions that are defined in the IDL interface *HELLO_ORB::HELLO_Gen*.

```python
HELLO_ORB::status HELLO::hello( const char* name )
{
...
}
HELLO_ORB::status HELLO::goodbye( const char* name )
{
...
}
```

In addition, `HELLO.cxx` implements a factory function which is used by the SALOME container to create an instance of the HELLO CORBA engine by demand:

```python
extern "C"
{
  PortableServer::ObjectId* HELLOEngine_factory( 
    CORBA::ORB_ptr orb,
    PortableServer::POA_ptr poa, 
    PortableServer::ObjectId* contId,
 const char* instanceName, 
 const char* interfaceName )
  {
    HELLO* component = new HELLO( orb, poa, contId, instanceName, interfaceName );
 return component->getId();
  }
}
```

- `src/HELLOGUI` sub-directory

This directory contains the C++ source files that implement the GUI library of HELLO module. By default, the name of the module GUI library is predefined and should be set as `lib<MODULE>`.so where `MODULE` is a name of the module. In the case of the HELLO module, the name of the GUI library should be `libHELLO.so`. It is also possible to use custom name of the GUI library of a module, but in this case, in order to be possible to use this module in SALOME GUI desktop, the name of the GUI library should be defined in the `SalomeApp.xml` file, in the module's main section, using *"library"* parameter, for example:

```python
<section name="HELLO">
  <parameter name="name" value="Hello"/>
  <parameter name="icon" value="HELLO.png"/>
  <parameter name="library" value="libMyHelloGUIlibrary.so"/>
</section>
```

The implementation of GUI library of the HELLO module should be done according to the architecture and rules specified by the SALOME GUI module. The main GUI module class (a\ HELLOGUI in our case) should be derived from the *SalomeApp_Module* class.

The developer has to redefine a set of methods which define the module behavior in GUI, for example, create menus, toolbars, define context popup menus, objects selection behavior, implement dialog boxes etc.

Here below is a short description of these methods. For more details please refer to the SALOME GUI module documentation.

- *initialize()* - module initialization; usually used to create GUI actions, menus, toolbars and so on;
- *activateModule()* - module activation; perform actions which should be done when the module is activated by the user, for example, show related menus and toolbars;
- *deactivateModule()* - module deactivation; perform actions which should be done when the module is deactivated by the user, for example, hide related menus and toolbars;
- *windows()* - get a list and a position of the dockable windows to be associated with the module; these windows will be automatically opened and positioned according to the settings defined by the value returned by this function;
- *viewManagers()* - get a list of the compatible viewers; these viewers will be automatically opened/raised on the module activation;
- *contextMenuPopup()* - create and return context popup menu according to the current selection;
- *createPreferences()* - initialize module's preferences;
- *preferencesChanged()* - callback function that is called when some module's preference is changed by the user; allows to perform the corresponding actions;
- *createSelection()* - create and return menu selection object; this is a part of the context popup menu definition API;
- *engineIOR()* - get the reference to the module CORBA engine;
- *moduleIcon()* and *iconName()* - these methods can be used to customize the module's main icon;
- *displayer()* - get the reference to the module's *Displayer* class; this is the part of common Show/Hide functionality mechanism;
- *storeVisualParameters()* and *restoreVisualParameters()* - these methods can be redefined to store/restore different visualization attributes of the presentable data if it is supported by the module, for example transparency, colors, display mode and other presentable parameters;
- *canCopy()*, *copy()*, *canPaste()*, *paste()* - these methods are the part of the common Copy/Paste functionality;
- *isDraggable()*, *isDropAccepted()*, *dropObjects()* - these methods are the part of the common Drag-n-Drop functionality;
- *createOperation()* - this function can be used as a part of the transaction-based operations mechanism.
- *renameAllowed()*, *renameObject()* - can be used for in-place (Object browser) renaming of the data entities, if it is supported by the module.

Note, that all of these methods are optional and need not be obligatory implemented because *SalomeApp_Module* class provides a base implementation of these functions. It's sometimes enough to implement only some of them, depending on the module needs.

In the case of HELLO module, only the following methods are implemented (other ones are just stubs, added for sample reasons):

- *engineIOR()* that initializes HELLO module's engine:

```python
QString HELLOGUI::engineIOR() const
{
  init(); // initialize engine, if necessary
  CORBA::String_var anIOR = getApp()->orb()->object_to_string( myEngine.in() );
 return QString( anIOR.in() );
}
```

- *initialize()* that creates actions, menus and toolbars for module's services service:

```python
void HELLOGUI::initialize( CAM_Application* app )
{
 // call the parent implementation
  SalomeApp_Module::initialize( app );

 // get reference to the desktop (used as a parent for actions)
  QWidget* dsk = app->desktop();
 // get resources manager
  SUIT_ResourceMgr* resMgr = app->resourceMgr();

 // create actions
 // ... Test me operation
  createAction( OpTestMe,                                               // operation id
                tr( "TLT_OP_TESTME" ),                                  // tooltip
                resMgr->loadPixmap( "HELLO",tr( "ICON_OP_TESTME" ) ),   // icon
                tr( "MEN_OP_TESTME" ),                                  // menu title
                tr( "STS_OP_TESTME" ),                                  // status tip
                0,                                                      // accelerator (not set)
                dsk,                                                    // parent
 false,                                                  // togglable flag (no)
 this,                                                   // action receiver
                SLOT( testMe() ) );                                     // action slot
 // create other actions ............

 // create menus
 int menuId;
  menuId = createMenu( tr( "MEN_FILE" ), -1, -1 );                      // File menu
  createMenu( separator(), menuId, -1, 10 );                            // add separator to File menu
  menuId = createMenu( tr( "MEN_FILE_HELLO" ), menuId, -1, 10 );        // File - Hello submenu
  createMenu( OpTestMe, menuId );                                       // File - Hello - Test me
 // create other menus ............

 // create toolbars
 int aToolId;
  aToolId = createTool ( tr( "TOOL_TEST" ) );                           // Test toolbar
  createTool( OpTestMe, aToolId );                                      // Test - Test me
 // create other toolbars ............

 // set-up popup menu
  QtxPopupMgr* mgr = popupMgr();
  mgr->insert( action( OpHello ),   -1, -1 );                           // Hello
  mgr->setRule( action( OpHello ),   baseRule + " and isComponent",  QtxPopupMgr::VisibleRule );
 // create other popup menu commands ............
}
```

- *activateModule()* that activates menus and toolbars

```python
bool HELLOGUI::activateModule( SUIT_Study* theStudy )
{
 // call parent implementation
 bool bOk = SalomeApp_Module::activateModule( theStudy );

 // show own menus
  setMenuShown( true );
 // show own toolbars
  setToolShown( true );

 // return the activation status
 return bOk;
}
```

- *deactivateModule()* that deactivates menus and toolbars

```python
bool HELLOGUI::deactivateModule( SUIT_Study* theStudy )
{
 // hide own menus
  setMenuShown( false );
 // hide own toolbars
  setToolShown( false );

 // call parent implementation and return the activation status
 return SalomeApp_Module::deactivateModule( theStudy );
}
```

- *windows()* that set-ups dockable windows requested by the module

```python
void HELLOGUI::windows( QMap<int, int>& theMap ) const
{
 // want Object browser, in the left area
  theMap.insert( SalomeApp_Application::WT_ObjectBrowser,
           Qt::LeftDockWidgetArea );
 // want Python console, in the bottom area
  theMap.insert( SalomeApp_Application::WT_PyConsole,
           Qt::BottomDockWidgetArea );
}
```

- *isDragable()*, *isDropAccepted()* and *dropObjects()* methods that handle the Drag-n-Drop operation

```python
bool HELLOGUI::isDragable( const SUIT_DataObject* what ) const
{
 // we allow dragging any HELLO object, except the top-level component
 const SalomeApp_ModuleObject* aModObj = dynamic_cast<const SalomeApp_ModuleObject*>( what );
 return ( aModObj == 0 );
}

bool HELLOGUI::isDropAccepted( const SUIT_DataObject* where ) const
{
 // we allow dropping of all objects
 return true;
}

void HELLOGUI::dropObjects( const DataObjectList& what, SUIT_DataObject* where,
 const int row, Qt::DropAction action )
{
 if (action != Qt::CopyAction && action != Qt::MoveAction)
 return; // unsupported action

 // get parent object
  SalomeApp_DataObject* dataObj = dynamic_cast<SalomeApp_DataObject*>( where );
 if ( !dataObj ) return; // wrong parent
  _PTR(SObject) parentObj = dataObj->object();

 // collect objects being dropped
  HELLO_ORB::object_list_var objects = new HELLO_ORB::object_list();
  objects->length( what.count() );
 int count = 0;
 for ( int i = 0; i < what.count(); i++ ) {
    dataObj = dynamic_cast<SalomeApp_DataObject*>( what[i] );
 if ( !dataObj ) continue;  // skip wrong objects
    _PTR(SObject) sobj = dataObj->object();
    objects[i] = _CAST(SObject, sobj)->GetSObject();
    count++;
  }
  objects->length( count );

 // call engine function
  engine()->copyOrMove( objects.in(),                              // what
               _CAST(SObject, parentObj)->GetSObject(),   // where
               row,                                       // row
               action == Qt::CopyAction );                // isCopy

 // update Object browser
  getApp()->updateObjectBrowser( false );
}
```

An implemention of the *hello()* and *goodbye()* methods is quite simple. These operations show the dialog box proposing the user to enter the name and pass the name entered by the user to the engine side, using the corresponding CORBA service.

```python
void HELLOGUI::hello()
{
 // request user name
 bool ok;
  QString name = QInputDialog::getText( getApp()->desktop(), tr( "QUE_HELLO_TITLE" ), tr( "QUE_ENTER_NAME" ),
                         QLineEdit::Normal, QString::null, &ok );

 if ( ok && !name.trimmed().isEmpty() ) {
 // say hello to SALOME
    HELLO_ORB::status status = engine()->hello( (const char*)name.toLatin1() );

 // update Object browser
    getApp()->updateObjectBrowser(true);

 // process operation status
 switch( status ) {
 case HELLO_ORB::OP_OK:
 // everything's OK
      SUIT_MessageBox::information( getApp()->desktop(),
                        tr( "INF_HELLO_TITLE" ), 
                        tr( "INF_HELLO_MSG" ).arg( name ),
                        tr( "BUT_OK" ) );
 break;
 case HELLO_ORB::OP_ERR_ALREADY_MET:
 // error: already said hello
      SUIT_MessageBox::warning( getApp()->desktop(),
                    tr( "INF_HELLO_TITLE" ), 
                    tr( "ERR_HELLO_ALREADY_MET" ).arg( name ),
                    tr( "BUT_OK" ) );
 break;
 case HELLO_ORB::OP_ERR_UNKNOWN:
 default:
 // other errors
      SUIT_MessageBox::critical( getApp()->desktop(),
                     tr( "INF_HELLO_TITLE" ), 
                     tr( "ERR_ERROR" ),
                     tr( "BUT_OK" ) );
 break;
    }
  }
}

void HELLOGUI::goodbye()
{
  SalomeApp_Application* app = dynamic_cast<SalomeApp_Application*>( application() );
  SalomeApp_Study* study = dynamic_cast<SalomeApp_Study*>( application()->activeStudy() );
  _PTR(Study) studyDS = study->studyDS();
  LightApp_SelectionMgr* aSelMgr = app->selectionMgr();

  QString name;

 // get selection
  SALOME_ListIO selected;
  aSelMgr->selectedObjects( selected );
 if ( selected.Extent() == 1 ) {
    Handle(SALOME_InteractiveObject) io = selected.First();
    _PTR(SObject) so = studyDS->FindObjectID( io->getEntry() );
 if ( so ) { 
      _PTR(SComponent) comp = so->GetFatherComponent();
 if ( comp && comp->ComponentDataType() == "HELLO" && io->getEntry() != comp->GetID() ) {
     name = so->GetName().c_str();
      }
    }
  }

 // request user name if not specified
 if ( name.isEmpty() ) {
 bool ok;
    name = QInputDialog::getText( getApp()->desktop(), tr( "QUE_GOODBYE_TITLE" ), tr( "QUE_ENTER_NAME" ),
                      QLineEdit::Normal, QString::null, &ok );
  }

 if ( !name.trimmed().isEmpty() ) {
 // say goodby to SALOME
    HELLO_ORB::status status = engine()->goodbye( (const char*)name.toLatin1() );

 // update Object browser
    getApp()->updateObjectBrowser(true);

 // process operation status
 switch( status ) {
 case HELLO_ORB::OP_OK:
 // everything's OK
      SUIT_MessageBox::information( getApp()->desktop(),
                        tr( "INF_GOODBYE_TITLE" ), 
                        tr( "INF_GOODBYE_MSG" ).arg( name ),
                        tr( "BUT_OK" ) );
 break;
 case HELLO_ORB::OP_ERR_DID_NOT_MEET:
 // error: did not say hello yet
      SUIT_MessageBox::warning( getApp()->desktop(),
                    tr( "INF_GOODBYE_TITLE" ), 
                    tr( "ERR_GOODBYE_DID_NOT_MEET" ).arg( name ),
                    tr( "BUT_OK" ) );
 break;
 case HELLO_ORB::OP_ERR_UNKNOWN:
 default:
 // other errors
      SUIT_MessageBox::critical( getApp()->desktop(),
                     tr( "INF_GOODBYE_TITLE" ), 
                     tr( "ERR_ERROR" ),
                     tr( "BUT_OK" ) );
 break;
    }
  }
}
```

Also, `HELLOGUI.cxx` provide an implementation of a factory function that is used by the SALOME GUI to create an instance of the HELLO GUI class by demand. It implements also another factory function to retrieve the version number of the module (in the About dialog box for example):

```python
extern "C" {
  CAM_Module* createModule()
  {
 return new HELLOGUI();
  }

 char* getModuleVersion() 
  {
 return (char*)HELLO_VERSION_STR;
  }
}
```

[<< Previous](idl_dir.md)  
[>> Next](bin_dir.md)
