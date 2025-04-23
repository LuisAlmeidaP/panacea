CoordX := 500
CoordY := 800

Type_presentation_x := 550
Type_presentation_y := 200

Date_request_patient_x := 960
Date_request_patient_y := 255

Press_modal_DHP_x := 1510
Press_modal_DHP_y := 530

Date_initial_x := 560
Date_initial_y := 370

Date_end_x := 950
Date_end_y := 370

Hour_initial_x := 560
Hour_initial_y := 420

Hour_end_x := 950
Hour_end_y := 420

Press_show_x := 1230
Press_show_y := 440

Accept_x = 885
Accept_y = 700


SetTitleMatchMode, 2 
IfWinExist, ahk_exe msedge.exe ahk_class Chrome_WidgetWin_1, :::: Panacea::::
{
    WinActivate 
    WinWaitActive
    Sleep, 300 

    CoordMode, Mouse, Screen
    MouseMove, %CoordX%, %CoordY%, 10
    Click 

    Sleep, 8000
    CoordMode, Mouse, Window  
    MouseMove, 300, 300  
    Sleep, 100
    Loop, 18
    {
        Send, {WheelDown}
        Sleep, 100
    }

    CoordMode, Mouse, Screen
    MouseMove, %Type_presentation_x%, %Type_presentation_y%, 10
    Sleep, 200
    Click
    Send, Cita 30 minutos
    Sleep, 200
    Send, {Enter}


    CoordMode, Mouse, Screen
    MouseMove, %Date_request_patient_x%, %Date_request_patient_y%, 10
    Sleep, 200
    Click
    Send, 29/04/2025
    Sleep, 200
    Send, {Enter}

    CoordMode, Mouse, Screen
    MouseMove, %Press_modal_DHP_x%, %Press_modal_DHP_y%, 10
    Sleep, 200
    Click
    Sleep, 200


    MouseMove, %Date_initial_x%, %Date_initial_y%, 10
    Sleep, 200
    Click
    Send, {Delete}
    Sleep, 100
    Send, 29/04/2025
    Sleep, 300

    MouseMove, %Date_end_x%, %Date_end_y%, 10
    Sleep, 200
    Click
    Send, {Delete}
    Sleep, 100
    Send, 29/04/2025
    Sleep, 300


    check_X := 325
    check_Y := 420
    MouseMove, %check_X%, %check_Y%, 10
    Sleep, 200
    Click
    Sleep, 200

    MouseMove, %Hour_initial_x%, %Hour_initial_y%, 10
    Sleep, 200
    Click
    Send, ^a
    Sleep, 100
    Send, {Delete}
    Sleep, 100
    Send, 6:00 am
    Sleep, 300

    MouseMove, %Hour_end_x%, %Hour_end_y%, 10
    Sleep, 200
    Click
    Send, ^a
    Sleep, 100
    Send, {Delete}
    Sleep, 100
    Send, 6:30 am
    Sleep, 300


    MouseMove, %Press_show_x%, %Press_show_y%, 10
    Sleep, 200
    Click

    schedule_x := 1230
    schedule_y := 540
    Sleep, 2000
    MouseMove, %schedule_x%, %schedule_y%, 10
    Send, {WheelDown}
    Sleep, 200
    Click
    Sleep, 10000


    MouseMove, %Accept_x%, %Accept_y%, 10
    Sleep, 300
    Click



}
else
{
    MsgBox, No se encontró una ventana de Edge con el título ":::: Panacea::::"
}
