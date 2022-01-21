# -*- coding: utf-8 -*-

import os
import datetime
import wx


def execute_cmd_in_shell(cmd_line):
    print('Received:\n\t{0}\n'.format(cmd_line))
    print(os.system(cmd_line))


def callback(url_string):
    chrome_app = '/Applications/Google Chrome.app'
    cmd_line = 'open -na "{0}" --args --new-window --args --window-size=1440,1200 "{1}"'.format(chrome_app, url_string)
    execute_cmd_in_shell(cmd_line)


def return_branch_string(branch_type):
    if branch_type == 'master':
        return 'CURRENT_RELEASE={0}&CURRENT_RELEASE_BRANCH=master'.format(current_version)
    elif branch_type == 'released':
        return 'CURRENT_RELEASE={0}&CURRENT_RELEASE_BRANCH={0}'.format(current_released_version)


def trigger_standalone_automation(branch_type, browser):
    job_name = 'neocore-dc2-automation'
    cmd_line = 'curl -I -X POST ' \
               '"https://{0}@{1}/{2}/{3}/buildWithParameters?' \
               '{4}&BROWSER={5}&VM_USERNAME=system&VM_PASSWORD=hoofkick&WEBDRIVERIO_LOG_LEVEL=silent"'.format(
                    jenkins_token,
                    jenkins_url,
                    jenkins_folder_name,
                    job_name,
                    return_branch_string(branch_type),
                    browser)
    execute_cmd_in_shell(cmd_line)


def trigger_integration_automation(branch_type, browser):
    job_name = 'neocore-dc2-automation-integration'
    cmd_line = 'curl -I -X POST ' \
               '"https://{0}@{1}/{2}/{3}/buildWithParameters?' \
               '{4}&BROWSER={5}&WEBDRIVERIO_LOG_LEVEL=silent"'.format(
                    jenkins_token,
                    jenkins_url,
                    jenkins_folder_name,
                    job_name,
                    return_branch_string(branch_type),
                    browser)
    execute_cmd_in_shell(cmd_line)


jenkins_url = 'jenkins.servicemax.com'
jenkins_folder_name = 'job/ServiceBoard/job'
jenkins_token = 'james.yang%40servicemax.com:113b53640d12c0c69c0d9f4ec004289850'
current_version = '22.1.0'
current_released_version = '21.2.0'


class AutomationPanel(wx.Frame):

    def __init__(self, parent):
        super(AutomationPanel, self).__init__(
            parent,
            title='Tool Panel :::::: James'.format(datetime.datetime.today().isoformat()),
            size=wx.Size(535, 285),
            style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        )

        panel = wx.Panel(self)
        gbs = wx.GridBagSizer(vgap=0, hgap=0)

        # row number of Standalone
        row_number_of_standalone = 1

        def create_mark():
            return wx.StaticText(panel, label='••>')

        def set_grid_bag_sizer_for_marks(row_number, col):
            gbs.Add(create_mark(), pos=(row_number, col), flag=wx.ALIGN_CENTER_VERTICAL, border=2)
            gbs.Add(create_mark(), pos=(row_number + 1, col), flag=wx.ALIGN_CENTER_VERTICAL, border=2)
            gbs.Add(create_mark(), pos=(row_number + 2, col), flag=wx.ALIGN_CENTER_VERTICAL, border=2)

        def create_button(button_size=(150, 25)):
            return [
                wx.Button(panel, id=wx.ID_ANY, label='Chrome', size=button_size),
                wx.Button(panel, id=wx.ID_ANY, label='Firefox', size=button_size),
                wx.Button(panel, id=wx.ID_ANY, label='Microsoft Edge', size=button_size)]

        def set_grid_bag_sizer_for_buttons(button_list, row_number, col, border=1):
            gbs.Add(button_list[0], pos=(row_number, col), flag=wx.ALL, border=border)
            gbs.Add(button_list[1], pos=(row_number + 1, col), flag=wx.ALL, border=border)
            gbs.Add(button_list[2], pos=(row_number + 2, col), flag=wx.ALL, border=border)

        # label: Master & Released
        label_title = wx.StaticText(panel, label='Test Suite')
        label_master = wx.StaticText(panel, label='Master')
        label_released = wx.StaticText(panel, label='Released')

        title_font = wx.Font(12, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD)
        label_title.SetFont(title_font)
        label_master.SetFont(title_font)
        label_released.SetFont(title_font)

        gbs.Add(label_title, pos=(0, 0), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,)
        gbs.Add(label_master, pos=(0, 2), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,)
        gbs.Add(label_released, pos=(0, 3), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,)

        # label: Standalone
        label_standalone = wx.StaticText(panel, label='standalone')
        label_standalone.SetForegroundColour((0, 0, 255))
        gbs.Add(
            label_standalone,
            pos=(row_number_of_standalone, 0),
            span=(3, 1),
            flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,
            border=1)
        label_standalone.Bind(wx.EVT_BUTTON, lambda e: callback(
            'https://{0}/{1}/neocore-dc2-automation/'.format(jenkins_url, jenkins_folder_name)))

        # marks
        set_grid_bag_sizer_for_marks(row_number_of_standalone, 1)

        # button group: standalone > master
        [std_master_chrome, std_master_firefox, std_master_ms_edge] = create_button()
        set_grid_bag_sizer_for_buttons(
            [std_master_chrome, std_master_firefox, std_master_ms_edge],
            row_number_of_standalone,
            2
        )
        std_master_chrome.Bind(wx.EVT_BUTTON, lambda e: trigger_standalone_automation('master', 'chrome'))
        std_master_firefox.Bind(wx.EVT_BUTTON, lambda e: trigger_standalone_automation('master', 'firefox'))
        std_master_ms_edge.Bind(wx.EVT_BUTTON, lambda e: trigger_standalone_automation('master', 'ms-edge'))

        # button group: standalone > released
        [std_released_chrome, std_released_firefox, std_released_ms_edge] = create_button()
        set_grid_bag_sizer_for_buttons(
            [std_released_chrome, std_released_firefox, std_released_ms_edge],
            row_number_of_standalone,
            3
        )
        std_released_chrome.Bind(wx.EVT_BUTTON, lambda e: trigger_standalone_automation('released', 'chrome'))
        std_released_firefox.Bind(wx.EVT_BUTTON, lambda e: trigger_standalone_automation('released', 'firefox'))
        std_released_ms_edge.Bind(wx.EVT_BUTTON, lambda e: trigger_standalone_automation('released', 'ms-edge'))

        # column number of Integration
        row_number_of_integration = row_number_of_standalone+4

        # label: Integration
        label_integration = wx.StaticText(panel, label='integration')
        label_integration.SetForegroundColour((0, 0, 255))
        gbs.Add(
            label_integration,
            pos=(row_number_of_integration, 0),
            span=(3, 1),
            flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL,
            border=1
        )

        # marks
        set_grid_bag_sizer_for_marks(row_number_of_integration, 1)

        # button group: integration > master
        [int_master_chrome, int_master_firefox, int_master_ms_edge] = create_button()
        set_grid_bag_sizer_for_buttons(
            [int_master_chrome, int_master_firefox, int_master_ms_edge],
            row_number_of_integration,
            2
        )
        int_master_chrome.Bind(wx.EVT_BUTTON, lambda e: trigger_integration_automation('master', 'chrome'))
        int_master_firefox.Bind(wx.EVT_BUTTON, lambda e: trigger_integration_automation('master', 'firefox'))
        int_master_ms_edge.Bind(wx.EVT_BUTTON, lambda e: trigger_integration_automation('master', 'ms-edge'))

        # button group: integration > released
        [int_released_chrome, int_released_firefox, int_released_ms_edge] = create_button()
        set_grid_bag_sizer_for_buttons(
            [int_released_chrome, int_released_firefox, int_released_ms_edge],
            row_number_of_integration,
            3
        )
        int_released_chrome.Bind(wx.EVT_BUTTON, lambda e: trigger_integration_automation('released', 'chrome'))
        int_released_firefox.Bind(wx.EVT_BUTTON, lambda e: trigger_integration_automation('released', 'firefox'))
        int_released_ms_edge.Bind(wx.EVT_BUTTON, lambda e: trigger_integration_automation('released', 'ms-edge'))

        # font setting for the note
        note_font = wx.Font(12, family=wx.DEFAULT, style=wx.ITALIC, weight=wx.BOLD)

        # label to show the version: label
        label_master_version = wx.StaticText(panel, label='  Master (build version):')
        label_released_version = wx.StaticText(panel, label='  Last Released (build version):')
        label_master_version.SetFont(note_font)
        label_master_version.SetForegroundColour((255, 0, 0))
        label_released_version.SetFont(note_font)
        label_released_version.SetForegroundColour((255, 0, 0))

        gbs.Add(label_master_version, pos=(row_number_of_integration+4, 0), border=2)
        gbs.Add(label_released_version, pos=(row_number_of_integration+5, 0), border=2)

        # label to show the version: version
        label_master_version_number = wx.StaticText(panel, label=current_version)
        label_released_version_number = wx.StaticText(panel, label=current_released_version)
        label_master_version_number.SetFont(note_font)
        label_master_version_number.SetForegroundColour((255, 0, 0))
        label_released_version_number.SetFont(note_font)
        label_released_version_number.SetForegroundColour((255, 0, 0))

        gbs.Add(label_master_version_number, pos=(row_number_of_integration+4, 2), border=2)
        gbs.Add(label_released_version_number, pos=(row_number_of_integration+5, 2), border=2)

        # Set Sizer
        panel.SetSizerAndFit(gbs)


def main():
    app = wx.App()
    instance = AutomationPanel(None)
    instance.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
