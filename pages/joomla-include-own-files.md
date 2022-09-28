# Integrate own files in Joomla
<!-- date: 2015-09-24 00:00:00 -->
<!-- category: joomla -->
<!-- tags: Joomla -->
Put the following code to the own Joomla files to integrate them to the CMS. After that you can include them by a wrapper.

    php
    define( '_JEXEC', 1);
    define('JPATH_BASE', dirname(__FILE__).'/..' );
    //this is when we are in the root
    define( 'DS', DIRECTORY_SEPARATOR );

    require_once ( JPATH_BASE .DS.'includes'.DS.'defines.php' );
    require_once ( JPATH_BASE .DS.'includes'.DS.'framework.php' );

    $mainframe =& JFactory::getApplication('site');
    $mainframe->initialise();
    $user = JFactory::getUser();

    echo  $user->username;
    ?>"
In case of the position of the file you have to edit the 'dirname'.
