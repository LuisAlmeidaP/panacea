CoordX := 800
CoordY := 600

SetTitleMatchMode, 2  
IfWinExist, ahk_exe msedge.exe ahk_class Chrome_WidgetWin_1, :::: Panacea::::
{
    WinActivate  
    WinWaitActive  
    Sleep, 300  

    
    CoordMode, Mouse, Window  
    MouseMove, 300, 300  
    Sleep, 100
    Loop, 10  
    {
        Send, {WheelDown}
        Sleep, 100
    }

    
    CoordMode, Mouse, Screen  
    MouseMove, %CoordX%, %CoordY%, 10  
    Sleep, 200
    Click  
}
else
{
    MsgBox, No se encontró una ventana de Edge con el título ":::: Panacea::::"
}
