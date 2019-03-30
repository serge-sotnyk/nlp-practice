Работа с принтером
==================

* [Получение списка принтеров](#GetPrinters)
* [Программирование банков памяти метки](#WriteMultipleBlocksLabelElement)
* [Программирование EPC форматами данных GS1/UNISCAN](#Gs1)
* [Управление доступом, блокировка метки](#Access)
* [Графическая персонализация](#Graphic)


<a name="GetPrinters"></a>
Получение списка принтеров
--------------------------
Получить список доступных в Шине RFID принтеров можно через запрос загруженных принтеров GetPrinters.



```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
...
printers = rfidbus.GetPrinters();
For each printer In printers Do
		Message(" Name: " + printer.Name
            + "; description " + printer.Description
			+ "; model description name: " + printer.ModelDescription.Name
			+ "; model description id: " + printer.ModelDescription.Id
			+ "; model description detail: " + printer.ModelDescription.Description
			);
EndDo;
```

<a name="WriteMultipleBlocksLabelElement"></a>
Программирование банков памяти метки
------------------------------------

Запись произвольных данных в банки памяти метки реализована через элемент WriteMultipleBlocksLabelElement.

```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
...
label = New COMObject("RfidBus.PrintLabel");
label.Width = 50;
label.Height = 50;

TransponderBank_Reserved   = 0;
TransponderBank_Epc        = 1;
TransponderBank_Tid        = 2;
TransponderBank_UserMemory = 3;

epcDataByteArray = New Array(4);
epcDataByteArray[0] = 100;
epcDataByteArray[1] = 100;
epcDataByteArray[2] = 100;
epcDataByteArray[3] = 100;

epc = New COMObject("RfidBus.WriteMultipleBlocksLabelElement");
epc.Data = New COMSafeArray(epcDataByteArray, "VT_UI1");
epc.StartingBlock = 2; // 0 -- R/O CRC; 1 -- PC; 2+ -- EPC
epc.WriteCount = epcDataByteArray.Count();
epc.MemoryBank = TransponderBank_Epc;
label.Elements.Add(epc);

printers = rfidbus.GetPrinters();
printer = printers[0];
printerTaskId = rfidbus.EnqueuePrintLabelTask(printer, label);
```

<a name="Gs1"></a>
Программирование EPC форматами данных GS1/UNISCAN
-------------------------------------------------

В Шине RFID реализованы запросы для программирования банка EPC специализированными форматами, такими как SGTIN, GIAI и др.
Пример записи средствами принтера данных  в память метки в формате GIAI-96:

```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
...
label = New COMObject("RfidBus.PrintLabel");
label.Width = 50;
label.Height = 50;
...
epc = New COMObject("RfidBus.WriteEpcGiai96LabelElement");
epc.Gcp = 461000232;
epc.Asset = 2;
epc.Filter = 0;
epc.Partition = 3;

printers = rfidbus.GetPrinters();
printer = printers[0];
printerTaskId = rfidbus.EnqueuePrintLabelTask(printer, label);
```

<a name="Access"></a>
Управление доступом, блокировка метки
--------------------------

За установку паролей доступа и уничтожения метки отвечают классы SetAccessPasswordElement и SetKillPasswordElement соответственно.
Для блокировки определённых банков памяти меток используется класс LockTransponderBankElement, а при необходимости заблокировать все банки памяти метки - LockTransponderElement.

```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
...
label = New COMObject("RfidBus.PrintLabel");
label.Width = 50;
label.Height = 50;

accessPasswordByteArray = New Array(4);
accessPasswordByteArray[0] = 255;
accessPasswordByteArray[1] = 255;
accessPasswordByteArray[2] = 255;
accessPasswordByteArray[3] = 255;
accessPasswordSafeByteArray = New COMSafeArray(accessPasswordByteArray, "VT_UI1");

accessPassword = New COMObject("RfidBus.SetAccessPasswordElement");
accessPassword.newAccessPassword = accessPasswordSafeByteArray;
label.Elements.Add(accessPassword);

killPasswordByteArray = New Array(4);
killPasswordByteArray[0] = 255;
killPasswordByteArray[1] = 255;
killPasswordByteArray[2] = 255;
killPasswordByteArray[3] = 255;
killPasswordSafeByteArray = New COMSafeArray(killPasswordByteArray, "VT_UI1");

killPassword = New COMObject("RfidBus.SetKillPasswordElement");
killPassword.KillPassword = killPasswordSafeByteArray;
label.Elements.Add(killPassword);

TransponderBankLockType_Unlocked          = 0;
TransponderBankLockType_PermanentLocked   = 1;
TransponderBankLockType_Locked            = 2;
TransponderBankLockType_PermanentUnlocked = 3;

lockTransponder =  New COMObject("RfidBus.LockTransponderElement");
lockTransponder.LockType = TransponderBankLockType_Locked;
lockTransponder.AccessPassword = accessPasswordSafeByteArray;
label.Elements.Add(lockTransponder);

printers = rfidbus.GetPrinters();
printer = printers[0];
printerTaskId = rfidbus.EnqueuePrintLabelTask(printer, label);
```

<a name="Graphic"></a>
Графическая персонализация
--------------------------

При печати на метках имеется возможность добавлять такие элементы как текст, изображения, различные геометрические фигуры, штрихкоды.
Пример добавления текста на метку:

```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
label = New COMObject("RfidBus.PrintLabel");
...
text = New COMObject("RfidBus.TextElement");
text.Text = "RFID Bus";
text.X = 5;
text.Y = 20;
text.Width = 45;
text.Height = 25;
text.FontFamily = "Arial";
text.FontSize = 4;
label.Elements.Add(text);

printers = rfidbus.GetPrinters();
printer = printers[0];
printerTaskId = rfidbus.EnqueuePrintLabelTask(printer, label);
```

Пример добавления изображения на метку:

```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
label = New COMObject("RfidBus.PrintLabel");
...
imageByteArray = rfidbus.Base64ToByteArray("iVBORw0KGgoAAAANSUhEUgAAAJ4AAABDCAQAAADHLHQBAAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAACxMAAAsTAQCanBgAAASaSURBVHja7ZttbBRFGMd/e9RS+sJLlQRfIIJBLC0FY4KCUhGthJAoMb40jYoag0GRRNGGD34QP5iS6AdMfKliQsHGKDFgiIkUVIiRJgokCK2QXkOCiBiohdpWtPbWD7e9u53d7d3N7XZvt/O/D7czs7uz+7t5ZuZ5Zk7TdZQkFVEIxjC8HjbS51PdBUFH9zgddNJMqWp5MujgKKt9aX2R4KPDN3yRMKDzC18kHOj8wRdQeI0WdHF8Lyh46fUaC2xyS1mv4KVXGdst+ErZxm0KXqb4bvUVXaCnKmU0J/D5gS7gk+RhfP6gAy3oUZW/WMd6X9CFAJ6fUiGpHGREVXRAC+xLdBMzpcdRnvBE/svVNCmixIGNpuuwhLMjXm73LeZGmEgVNTxCSZrH+ZVDHKOLfv4hlz5jJh8ZR/PpNZVMo804WsZpN/o2qqhlFdOzh5edynmR1Y6t+Dve5yeXarqZvaMEbxhhHa8yxcs+7082sYFBm5LLrOEZ19CNvnQ+ZTk/ez1g7KLBktdHHfsCP0RcoJ5TXo+2u/lQyHmZk6EYYftZx4DXU5V3uZyS2heCVjesKFu9htfLJympraGa3zUbfbrt6lkx46Vu2mcaKPYnQpNXOJonr309E6SuO5cw1fig+AvVTvA28oRUFc/yTUqqg0GuMo7MU9WHWeMCiCKJaxq5S6qupzhoSh9zhueO/uUSUwH4QyiZzOyAG26P975tofE9FDqvdsi5zzvFfqlbXjSlSikj6Tmnqp1tLrzAtSzPj8CAWS20uHDrxY7Nui3hPuWiRb7D89BsHyTs8gxeBfcreLK6J+gbsPyE10S7gic/mH+g4MlrrxCiDJ9sO6bbJT2AA6aI9CA/cp/teQtZ5oqfmpfwVkr7tuZwfrfDedU8p8w2MycmvL2dWreVUomz2YZXrUSlrvtNSM8bi/B2uHKXCcxXZiurOiMQq+BlramJ5QUFL0uN4x2uVvDkerv3uGPkSbKSvSrYYvK9FLwMW1wN9dQIuZquw7f8LcxiZkhVcVhYJ6s2NmX9LqzbzqLC1Vd7U3j+SbyS8Lb7c7y3RjETmWu70Km21earb6vgKSl4XqgAoAmdedwpFO2km+msBKCHPZwWtk3H9Tp7OMEU1lpKNjPEYhbQ5Fh5IS/xGV22j1VJbWLHQb5K03WYCTzJJqFoBSdZwnagk3phN0BSUTbwJTfwvaXkJmKs5TGWjjAB6LBsoUmqkh2mHcABNdvNXAQitp90f0DQLOcm0wUpjyF+oJ0tQTDbdOoAHuJtqQpmpJjlThqAr7hFOKfYZpmylijHwwBvCPjaYR/7AQDOsdBSEsv4Ia7wqCXvLPHuJPDwAAZMeyOT0g1QF3J4iJjtD1M+yv/b9hDeNOY69Glxw1thKfkii453qSXnRp7muiDA09A5zw9CUT9wiRNUUQjM4fkRRpxy3rKU7MrYcIv4OLjzvFl00UqrTfFx3uBz7qaFgw5TiihjVxGAxjTzqQYWKXfCOaoyQBu9tv9BvMaIYh2h03YRu54jnKHEZpfmbmLMoTIl5wyHgXuZlJJ3iPMU8ECQ4SmpwMAo639+igg29pVEuAAAAABJRU5ErkJggg==");
image = New COMObject("RfidBus.ImageElement");
image.X = 1;
image.Y = 1;
image.Height = 16;
image.Width = 36;
image.ImageData = New COMSafeArray(imageByteArray.Unload(), "VT_UI1");
label.Elements.Add(image);

printers = rfidbus.GetPrinters();
printer = printers[0];
printerTaskId = rfidbus.EnqueuePrintLabelTask(printer, label);
```

В следующем примере рассматривается добавление на метку линии, с указанием начальных и конечных координат, толщины и цвета. Добавление других геометрических фигур производится аналогичным способом, различия заключаются только в параметрах фигур, например, для описания окружности (CircleElement) следует указать координаты центра и радиус.

```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
label = New COMObject("RfidBus.PrintLabel");
...
line = New COMObject("RfidBus.LineElement");
line.X1 = 1;
line.Y1 = 18;
line.X2 = 50;
line.Y2 = 18;
label.Elements.Add(line);

printers = rfidbus.GetPrinters();
printer = printers[0];
printerTaskId = rfidbus.EnqueuePrintLabelTask(printer, label);
```

Пример добавления штрихкода на метку. В данном случае применён стандарт Code 128.

```bsl
rfidbus = New COMObject("AddIn.RfidBus1cClient");
label = New COMObject("RfidBus.PrintLabel");
...
barcode = New COMObject("RfidBus.Code128BarCodeElement");
barcode.X = 5;
barcode.Y = 35;
barcode.Width = 40;
barcode.Height = 25;
barcode.CodeFontSize = 2;
barcode.ShowCodeText = True;
barcode.Value = "4610002321000";
label.Elements.Add(barcode);

printers = rfidbus.GetPrinters();
printer = printers[0];
printerTaskId = rfidbus.EnqueuePrintLabelTask(printer, label);
```

[⬅ К оглавлению](../README.md)

