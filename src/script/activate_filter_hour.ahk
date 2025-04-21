; Coordenadas deseadas
Coord1_X := 630
Coord1_Y := 660

Coord2_X := 1150
Coord2_Y := 660

Coord3_X := 320
Coord3_Y := 710

Coord4_X := 630
Coord4_Y := 710

Coord5_X := 1150
Coord5_Y := 710

Coord6_X := 1450
Coord6_Y := 740

SetTitleMatchMode, 2
IfWinExist, ahk_exe msedge.exe ahk_class Chrome_WidgetWin_1, :::: Panacea::::
{
    WinActivate
    WinWaitActive
    Sleep, 300
    CoordMode, Mouse, Screen

    ; ===== Primera coordenada =====
    MouseMove, %Coord1_X%, %Coord1_Y%, 10
    Sleep, 200
    Click
    Send, {Delete}
    Sleep, 100
    Send, 23/04/2025
    Sleep, 300

    ; ===== Segunda coordenada =====
    MouseMove, %Coord2_X%, %Coord2_Y%, 10
    Sleep, 200
    Click
    Send, {Delete}
    Sleep, 100
    Send, 23/04/2025
    Sleep, 300


    MouseMove, %Coord3_X%, %Coord3_Y%, 10
    Sleep, 200
    Click

    MouseMove, %Coord4_X%, %Coord4_Y%, 10
    Sleep, 200
    Click
    Send, ^a  ; Ctrl + A para seleccionar todo
    Sleep, 100
    Send, {Delete}  ; Borra el contenido seleccionado
    Sleep, 100
    Send, 6:00 am
    Sleep, 300
    
    MouseMove, %Coord5_X%, %Coord5_Y%, 10
    Sleep, 200
    Click
    Send, ^a
    Sleep, 100
    Send, {Delete}
    Sleep, 100
    Send, 6:30 am
    Sleep, 300


    MouseMove, %Coord6_X%, %Coord6_Y%, 10
    Sleep, 200
    Click

}
else
{
    MsgBox, No se encontró una ventana de Edge con el título ":::: Panacea::::"
}
