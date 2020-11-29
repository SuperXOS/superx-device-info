import QtQuick 2.15
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.2
import QtQuick.Window 2.12
import org.kde.kirigami 2.14 as Kirigami

Kirigami.Page {
    Kirigami.Card {
        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
            bottom: parent.bottom
            margins: 30
        }

        RowLayout {
            anchors.centerIn: parent
            width: parent.width
            ColumnLayout {
                id: os_info_layout
                Layout.alignment: Qt.AlignCenter
                Layout.fillWidth: true

                Kirigami.Icon {
                    Layout.alignment: Qt.AlignCenter
                    source: 'image-x-generic'
                    height: 128
                    width: height
                }

                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'SuperX x.x' // release of SuperX
                    font {
                        family: 'Roboto Slab'
                        pointSize: 22
                    }
                }
                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'Linux Kernel xx.xx' // kernel version in use
                }
                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'Qt x.xx.xx' // Qt version in use
                }
                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'Plasma x.xx.xx' // KDE Plasma version in use
                }

                Button {
                    Layout.alignment: Qt.AlignCenter
                    text: 'Get Help and Support'
                    icon.name: 'help-contents'
                }

            }

            Kirigami.Separator {
                Layout.fillHeight: true
            }

            ColumnLayout {
                id: hw_info_layout
                Layout.alignment: Qt.AlignCenter
                Layout.fillWidth: true

                Kirigami.Icon {
                    Layout.alignment: Qt.AlignCenter
                    source: 'image-x-generic'
                    height: 128
                    width: height
                }

                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'Hostname' // hostname of the computer
                    font {
                        family: 'Roboto Slab'
                        pointSize: 22
                    }
                }
                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'CPU' // Brand, Model and other generic CPU information
                }
                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'RAM' // Available system memory
                }
                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'GPU' // Brand, Model and other generic GPU information
                }

                Kirigami.Label {
                    Layout.alignment: Qt.AlignCenter
                    text: 'Storage' // Total available storage and type of root partition.
                }

            }

        }
    }
}
