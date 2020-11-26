import QtQuick 2.15
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.2
import QtQuick.Window 2.12
import org.kde.kirigami 2.14 as Kirigami

Kirigami.ApplicationWindow {
    id: root
    title: i18n("Device Information")

    pageStack {
        defaultColumnWidth: width
        separatorVisible: false
        globalToolBar.showNavigationButtons: false
    }

    globalDrawer: Kirigami.GlobalDrawer {
        id: sidebar
        title: "Device Information"
        modal: false
        width: Kirigami.Units.gridUnit * 10

        handleVisible: modal

        header: ToolBar {
            Layout.fillWidth: true
        }


        titleIcon: 'dialog-input-devices'
        collapseButtonVisible: true

        ListModel{ // TODO: Add i18n.
            id: deviceCategoies
            ListElement{title: 'Summary' ; icon: 'hwinfo'; keywords: 'summary'}
            ListElement{title: 'CPU' ; icon: 'cpu'; keywords: 'processor'}
            ListElement{title: 'Motherboard' ; icon: 'dashboard-show'; keywords: 'motherboard'}
            ListElement{title: 'RAM' ; icon: 'media-flash-memory-stick'; keywords: 'ram'}
            ListElement{title: 'Storage' ; icon: 'drive-harddisk'; keywords: 'storage'}
            ListElement{title: 'Display' ; icon: 'monitor'; keywords: 'display'}
            ListElement{title: 'Network' ; icon: 'network-modem'; keywords: 'network'}
            ListElement{title: 'Other PCI devices' ; icon: 'network-card'; keywords: 'other-pci'}
            ListElement{title: 'Battery ' ; icon: 'battery-050'; keywords: 'battery'}
            ListElement{title: 'Mouse' ; icon: 'input-mouse'; keywords: 'mouse'}
            ListElement{title: 'Keyboard' ; icon: 'input-keyboard'; keywords: 'keyboard'}
            ListElement{title: 'Printer' ; icon: 'printer'; keywords: 'printer'}
            ListElement{title: 'Camera' ; icon: 'camera-web'; keywords: 'camera'}
            ListElement{title: 'Other Devices' ; icon: 'drive-removable-media-usb-pendrive'; keywords: 'other-devices'}
        }

        Instantiator {
            model: deviceCategoies

            Kirigami.Action {
                text: model.title
                iconName: model.icon
                checkable: true

                onTriggered: {
                    Helper.navigateToPage(Qt.resolvedUrl('Information.qml'))

                    for (var i = 0; i < sidebar.actions.length; ++i ) {
                        sidebar.actions[i].checked = false;
                    }
                    checked = true;
                }
            }

            onObjectAdded: {
                var actions = Array.prototype.map.call(sidebar.actions, i => i)
                actions.splice(index, 0, object)
                sidebar.actions = actions
            }
        }
    }

    pageStack.initialPage: Kirigami.Page {
    }
}
