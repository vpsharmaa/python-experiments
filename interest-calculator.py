import wx
import math


class CompoundInterestFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            None,
            title="Compound Interest Calculator",
            size=(420, 350)
        )

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Principal
        vbox.Add(wx.StaticText(panel, label="Principal (P)"), 0, wx.ALL, 5)
        self.principal = wx.TextCtrl(panel)
        vbox.Add(self.principal, 0, wx.EXPAND | wx.ALL, 5)

        # Rate
        vbox.Add(wx.StaticText(panel, label="Rate of Interest (%) (R)"), 0, wx.ALL, 5)
        self.rate = wx.TextCtrl(panel)
        vbox.Add(self.rate, 0, wx.EXPAND | wx.ALL, 5)

        # Time
        vbox.Add(wx.StaticText(panel, label="Time in Years (T)"), 0, wx.ALL, 5)
        self.time = wx.TextCtrl(panel)
        vbox.Add(self.time, 0, wx.EXPAND | wx.ALL, 5)

        # Amount
        vbox.Add(wx.StaticText(panel, label="Amount (A)"), 0, wx.ALL, 5)
        self.amount = wx.TextCtrl(panel)
        vbox.Add(self.amount, 0, wx.EXPAND | wx.ALL, 5)

        # Button
        calc_btn = wx.Button(panel, label="Calculate Missing Value")
        calc_btn.Bind(wx.EVT_BUTTON, self.calculate)
        vbox.Add(calc_btn, 0, wx.ALL | wx.CENTER, 15)

        # Result
        self.result = wx.StaticText(panel, label="")
        vbox.Add(self.result, 0, wx.ALL, 10)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def calculate(self, event):
        fields = {
            "P": self.principal.GetValue().strip(),
            "R": self.rate.GetValue().strip(),
            "T": self.time.GetValue().strip(),
            "A": self.amount.GetValue().strip()
        }

        empty = [k for k, v in fields.items() if v == ""]

        if len(empty) != 1:
            wx.MessageBox(
                "Please leave exactly ONE field empty.",
                "Input Error",
                wx.OK | wx.ICON_ERROR
            )
            return

        try:
            P = float(fields["P"]) if fields["P"] else None
            R = float(fields["R"]) if fields["R"] else None
            T = float(fields["T"]) if fields["T"] else None
            A = float(fields["A"]) if fields["A"] else None

            if empty[0] == "A":
                A = P * (1 + R / 100) ** T
                self.amount.SetValue(f"{A:.2f}")
                self.result.SetLabel("Calculated Amount (A).")

            elif empty[0] == "P":
                P = A / ((1 + R / 100) ** T)
                self.principal.SetValue(f"{P:.2f}")
                self.result.SetLabel("Calculated Principal (P).")

            elif empty[0] == "R":
                R = ((A / P) ** (1 / T) - 1) * 100
                self.rate.SetValue(f"{R:.2f}")
                self.result.SetLabel("Calculated Rate of Interest (R).")

            elif empty[0] == "T":
                T = math.log(A / P) / math.log(1 + R / 100)
                self.time.SetValue(f"{T:.2f}")
                self.result.SetLabel("Calculated Time (T).")

        except Exception:
            wx.MessageBox(
                "Invalid values or mathematical error.",
                "Calculation Error",
                wx.OK | wx.ICON_ERROR
            )


if __name__ == "__main__":
    app = wx.App()
    CompoundInterestFrame()
    app.MainLoop()
