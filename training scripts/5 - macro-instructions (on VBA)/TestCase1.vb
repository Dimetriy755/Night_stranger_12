Sub TestCase1()
' TestCase1 Макрос
' Сочетание клавиш: Ctrl+й

    ' здесь cоздание таблицы происходит в новом листе
    ' + присваивание листу названия (через переменную)
    '
    Dim myList As Object
    Set myList = Worksheets.Add
    myList.Name = "Listok1"
    
    ' уменьшение масштаба страницы до 82 ед.
    '
    ActiveWindow.Zoom = 82
    
    ' общая рамка для всей таблицы
    '
    Range("A1:Q26").Select
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    ' все вертикальные линии таблицы
    '
    Range("B3:B4").Select
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("E5:E26").Select
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("K5:K9").Select
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("K11:K14").Select
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("K16:K23").Select
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("K25:K26").Select
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    ' все горизонтальные линии таблицы
    '
    Range("A3:Q3").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A4:Q4").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A10:Q10").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A11:Q11").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A12:Q12").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A13:Q13").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A14:Q14").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A15:Q15").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A16:Q16").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A17:Q17").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A18:Q18").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A19:Q19").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A20:Q20").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A21:Q21").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A22:Q22").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A23:Q23").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A24:Q24").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A25:Q25").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    Range("A26:Q26").Select
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlMedium
    End With
    
    ' заливка цветом определённого количества ячеек
    '
    Range("A10:Q10").Interior.Color = RGB(214, 220, 228)
    Range("A15:Q15").Interior.Color = RGB(214, 220, 228)
    Range("A24:Q24").Interior.Color = RGB(214, 220, 228)
    
    ' установка определённых условий на всю таблицу
    ' (у определённых слов сразу будут меняться цвета)
    '
    Range("A1:Q27").Select
    Selection.FormatConditions.Add Type:=xlTextString, String:="passed", _
    TextOperator:=xlContains
    Selection.FormatConditions(Selection.FormatConditions.Count).SetFirstPriority
    With Selection.FormatConditions(1).Font
        .Color = vbGreen
        .Bold = True
    End With
    Selection.FormatConditions(1).StopIfTrue = False
    
    Range("A1:Q27").Select
    Selection.FormatConditions.Add Type:=xlTextString, String:="failed", _
    TextOperator:=xlContains
    Selection.FormatConditions(Selection.FormatConditions.Count).SetFirstPriority
    With Selection.FormatConditions(1).Font
        .Color = vbRed
        .Bold = True
    End With
    Selection.FormatConditions(1).StopIfTrue = False
    
    Range("A1:Q27").Select
    Selection.FormatConditions.Add Type:=xlTextString, String:="blocked", _
    TextOperator:=xlContains
    Selection.FormatConditions(Selection.FormatConditions.Count).SetFirstPriority
    With Selection.FormatConditions(1).Font
        .Color = rgbCrimson
        .Bold = True
    End With
    Selection.FormatConditions(1).StopIfTrue = False
    
    Range("A1:Q27").Select
    Selection.FormatConditions.Add Type:=xlTextString, String:="no data", _
    TextOperator:=xlContains
    Selection.FormatConditions(Selection.FormatConditions.Count).SetFirstPriority
    With Selection.FormatConditions(1).Font
        .Color = rgbGray
        .Bold = True
    End With
    Selection.FormatConditions(1).StopIfTrue = False
    
    ' создание всего текста таблицы
    ' +  объединение ячеек в таблице
    ' +  установка вида, размера шрифта
    ' +  заливка цветом некоторого текста
    '
    Range("A1").Value = "Этот тест в дальнейшем будет автоматизирован"
    
    Range("A1:Q2").Select
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlTop
        .ReadingOrder = xlContext
        .MergeCells = True
    End With
    
    Range("A3").Value = "Название:"
    Range("A4").Value = "Проверки:"
    
    Range("C3:Q3").Select
    Selection.Merge
    
    Range("C4:Q4").Select
    Selection.Merge
    
    Range("A7").Value = "Действия:"
    Range("F7").Value = "Ожидаемый результат:"
    
    Range("A5:E9").Select
    Selection.Merge
    
    Range("A5:E9").Select
    Selection.VerticalAlignment = xlCenter
    
    Range("F5:K9").Select
    Selection.Merge
    
    Range("F5:K9").Select
    Selection.VerticalAlignment = xlCenter
    
    Range("L5").Value = "Все варианты каким может быть результат после проведения тестов:"
    
    Range("L5:Q6").Select
    With Selection
        .WrapText = True
        .MergeCells = True
    End With
    
    Range("A3:Q9").Select
    With Selection.Font
        .Size = 12
        .Bold = True
        .Name = "Times New Roman"
    End With
    
    Range("L7").Value = "· пройден"
    Range("L8").Value = "· провален"
    Range("L9").Value = "· заблокирован"
    
    Range("L7:Q7").Font.Color = vbGreen
    Range("L8:Q8").Font.Color = RGB(255, 0, 0)
    Range("L9:Q9").Font.Color = rgbCrimson
    
    Range("L7:Q7").Select
    With ActiveCell.Characters(Start:=1, Length:=1).Font
        .FontStyle = "обычный"
        .Name = "Symbol"
        .Color = vbBlack
    End With
    
    Range("L8:Q8").Select
    With ActiveCell.Characters(Start:=1, Length:=1).Font
        .FontStyle = "обычный"
        .Name = "Symbol"
        .Color = vbBlack
    End With
    
    Range("L9:Q9").Select
    With ActiveCell.Characters(Start:=1, Length:=1).Font
        .FontStyle = "обычный"
        .Name = "Symbol"
        .Color = vbBlack
    End With
    
    Range("L7:Q7").Select
    Selection.Merge
    Range("L8:Q8").Select
    Selection.Merge
    Range("L9:Q9").Select
    Selection.Merge
    
    Range("A10").Value = "Предусловие:"
    Range("A15").Value = "Шаги теста:"
    Range("A24").Value = "Постусловие:"
    
    Range("A1:H1").Select
    With Selection.Font
        .Size = 16
        .Bold = True
        .Name = "Times New Roman"
    End With
    
    Range("A10:E10").Select
    With Selection.Font
        .Size = 13
        .Bold = True
        .Name = "Times New Roman"
    End With
    
    Range("A15:E15").Select
    With Selection.Font
        .Size = 13
        .Bold = True
        .Name = "Times New Roman"
    End With
    
    Range("A24:E24").Select
    With Selection.Font
        .Size = 13
        .Bold = True
        .Name = "Times New Roman"
    End With
    
    ' левая часть таблицы
    '
    Range("A11:E11").Select
    Selection.Merge
    
    Range("A12:E12").Select
    Selection.Merge
    
    Range("A13:E13").Select
    Selection.Merge
    
    Range("A14:E14").Select
    Selection.Merge
    
    Range("A16:E16").Select
    Selection.Merge
    
    Range("A17:E17").Select
    Selection.Merge
    
    Range("A18:E18").Select
    Selection.Merge
    
    Range("A19:E19").Select
    Selection.Merge
    
    Range("A20:E20").Select
    Selection.Merge
    
    Range("A21:E21").Select
    Selection.Merge
    
    Range("A22:E22").Select
    Selection.Merge
    
    Range("A23:E23").Select
    Selection.Merge
    
    Range("A25:E25").Select
    Selection.Merge
    
    Range("A26:E26").Select
    Selection.Merge
    
    ' середина таблицы
    '
    Range("F11:K11").Select
    Selection.Merge
    
    Range("F12:K12").Select
    Selection.Merge
    
    Range("F13:K13").Select
    Selection.Merge
    
    Range("F14:K14").Select
    Selection.Merge
    
    Range("F16:K16").Select
    Selection.Merge
    
    Range("F17:K17").Select
    Selection.Merge
    
    Range("F18:K18").Select
    Selection.Merge
    
    Range("F19:K19").Select
    Selection.Merge
    
    Range("F20:K20").Select
    Selection.Merge
    
    Range("F21:K21").Select
    Selection.Merge
    
    Range("F22:K22").Select
    Selection.Merge
    
    Range("F23:K23").Select
    Selection.Merge
    
    Range("F25:K25").Select
    Selection.Merge
    
    Range("F26:K26").Select
    Selection.Merge
    
    ' правая часть таблицы
    '
    Range("L11:Q11").Select
    Selection.Merge
    
    Range("L12:Q12").Select
    Selection.Merge
    
    Range("L13:Q13").Select
    Selection.Merge
    
    Range("L14:Q14").Select
    Selection.Merge
    
    Range("L16:Q16").Select
    Selection.Merge
    
    Range("L17:Q17").Select
    Selection.Merge
    
    Range("L18:Q18").Select
    Selection.Merge
    
    Range("L19:Q19").Select
    Selection.Merge
    
    Range("L20:Q20").Select
    Selection.Merge
    
    Range("L21:Q21").Select
    Selection.Merge
    
    Range("L22:Q22").Select
    Selection.Merge
    
    Range("L23:Q23").Select
    Selection.Merge
    
    Range("L25:Q25").Select
    Selection.Merge
    
    Range("L26:Q26").Select
    Selection.Merge
    
    ' создание ещё одного листа с таблицей
    ' для заведения выпадающих списков
    ' + список присваивается переменной
    '
    Worksheets.Add

    Range("A1:A5").Select
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    Selection.Borders(xlInsideVertical).LineStyle = xlNone
    Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
    
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideVertical)
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideHorizontal)
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
    
    Range("A1").Interior.Color = RGB(146, 208, 80)
    
    Range("A1").Value = "Результат:"
    With Selection.Font
        .Size = 10
        .Bold = True
        .Name = "Times New Roman"
    End With
    
    Range("A2").Value = "passed"
    Range("A3").Value = "failed"
    Range("A4").Value = "blocked"
    Range("A5").Value = "no data"
    
    Range("A2:A5").Select
    With Selection.Font
        .Size = 9
        .Name = "Calibri"
        .FontStyle = "обычный"
    End With
    
    Columns("A:A").ColumnWidth = 12.12
    
    Range("A1:A5").Select
    ActiveSheet.ListObjects.Add(xlSrcRange, Range("A1:A5"), , xlYes).Name = _
    "result1"
    ActiveWorkbook.Names.Add Name:="list1", RefersToR1C1:="=result1[Результат:]"
    
    ' Здесь очень важный момент, происходит переход
    ' на ранее созданный лист, его название - "Listok1".
    ' И такое название у листа с тест-кейсом по скрипту
    ' будет всегда, поэтому если нужно больше одного
    ' тест-кейса, то при повторном запуске скрипта нужно
    ' будет переименовать - "Listok1" => "Listok" (пример).
    ' Если повторно попытаться создать тест-кейс с тем же
    ' названием, то будет ошибка. Можно переименовать
    ' созданный ранее лист в самом документе (удобнее)
    ' и создать новый - "Listok1" с новым тест-кейсом.
    '
    Sheets("Listok1").Select
    
    Range("L11:Q14").Select
    With Selection.Validation
        .Delete
        .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
        xlBetween, Formula1:="=list1"
    End With
    
    Range("L16:Q23").Select
    With Selection.Validation
        .Delete
        .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
        xlBetween, Formula1:="=list1"
    End With
    
    Range("L25:Q26").Select
    With Selection.Validation
        .Delete
        .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
        xlBetween, Formula1:="=list1"
    End With
    
End Sub
