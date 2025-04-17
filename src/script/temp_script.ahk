F9::
SetTitleMatchMode, 2  ; Permite buscar una parte del título
IfWinExist, Panacea - Internet Explorer
{
    WinActivate
    Sleep, 500

    ; Mueve el mouse a una posición en la ventana (ajusta si es necesario)
    CoordMode, Mouse, Window
    MouseMove, 600, 400  ; Coordenadas dentro de la ventana de Panacea
    Sleep, 300

    ; Realiza el scroll hacia abajo
    Loop, 5
    {
        Send, {WheelDown}
        Sleep, 100
    }
}
else
{
    MsgBox, ❌ No se encontró la ventana de Panacea.
}
return
