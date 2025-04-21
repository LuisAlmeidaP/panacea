; Coordenadas deseadas (ajusta a tu necesidad)
CoordX := 1820
CoordY := 830

; Buscar una ventana de Edge con el título que incluya ":::: Panacea::::"
SetTitleMatchMode, 2  ; Permite coincidencia parcial del título
IfWinExist, ahk_exe msedge.exe ahk_class Chrome_WidgetWin_1, :::: Panacea::::
{
    WinActivate  ; Activa la ventana
    WinWaitActive  ; Espera a que esté activa
    Sleep, 300  ; Pausa breve para asegurar que esté lista

    ; Hacer scroll hacia abajo (simula mover la rueda del mouse)
    CoordMode, Mouse, Window  ; Coordenadas relativas a la ventana (para el scroll)
    MouseMove, 300, 300  ; Mueve el mouse a un punto dentro de la ventana antes de hacer scroll
    Sleep, 100
    Loop, 10  ; Ajusta cuántas veces quieres scrollear
    {
        Send, {WheelDown}
        Sleep, 100
    }

    ; Mover el mouse y hacer clic
    CoordMode, Mouse, Screen  ; Coordenadas relativas a la pantalla
    MouseMove, %CoordX%, %CoordY%, 10  ; Mueve el mouse suavemente
    Sleep, 200
    Click  ; Clic izquierdo
}
else
{
    MsgBox, No se encontró una ventana de Edge con el título ":::: Panacea::::"
}
