import { app } from '/scripts/app.js';
import { api } from '/scripts/api.js';
import { commonPrefix } from './common.js';

class CrystoolsMonitor {
  idExtensionName = 'Crystools.monitor';
  menuPrefix = commonPrefix;
  htmlIdCrystoolsRoot = 'crystools-root';
  htmlIdCrystoolsMonitorContainer = 'crystools-monitor-container';

  idInputRate = 'Crystools.inputRate';
  defaultRate = .5;
  idWhichHDD = 'Crystools.whichHDD';
  defaultWhichHDD = '/';
  monitorGPUSettings: TMonitorSettings[] = [];
  monitorVRAMSettings: TMonitorSettings[] = [];
  monitorTemperatureSettings: TMonitorSettings[] = [];

  // CPU Variables
  monitorCPUElement: TMonitorSettings = {
    id: 'Crystools.switchCPU',
    name: this.menuPrefix + ' [monitor] CPU Usage',
    type: 'boolean',
    label: 'CPU',
    symbol: '%',
    defaultValue: true,
    htmlMonitorRef: undefined,
    htmlMonitorSliderRef: undefined,
    htmlMonitorLabelRef: undefined,
    cssColor: '#0AA015',
    onChange: async(value: boolean) => {
      this.updateWidget(this.monitorCPUElement);
      await this.updateServer({
        switchCPU: value,
      });
    },
  };

  // RAM Variables
  monitorRAMElement: TMonitorSettings = {
    id: 'Crystools.switchRAM',
    name: this.menuPrefix + ' [monitor] RAM Used',
    type: 'boolean',
    label: 'RAM',
    symbol: '%',
    defaultValue: true,
    htmlMonitorRef: undefined,
    htmlMonitorSliderRef: undefined,
    htmlMonitorLabelRef: undefined,
    cssColor: '#07630D',
    onChange: async(value: boolean) => {
      this.updateWidget(this.monitorRAMElement);
      await this.updateServer({
        switchRAM: value,
      });
    },
  };

  // HDD Variables
  monitorHDDElement: TMonitorSettings = {
    id: 'Crystools.switchHDD',
    name: this.menuPrefix + ' [monitor] HDD Used',
    type: 'boolean',
    label: 'HDD',
    symbol: '%',
    tooltip: 'See Partition to show (HDD)',
    defaultValue: true,
    htmlMonitorRef: undefined,
    htmlMonitorSliderRef: undefined,
    htmlMonitorLabelRef: undefined,
    cssColor: '#730F92',
    onChange: async(value: boolean) => {
      this.updateWidget(this.monitorHDDElement);
      await this.updateServer({
        switchHDD: value,
      });
    },
  };

  constructor() {
    this.createSettings();
  }

  createSettings = (): void => {
    app.ui.settings.addSetting(this.monitorCPUElement);
    app.ui.settings.addSetting(this.monitorRAMElement);
    app.ui.settings.addSetting(this.monitorHDDElement);

    app.ui.settings.addSetting({
      id: this.idInputRate,
      name: this.menuPrefix + '[monitor] Refresh rate',
      tooltip: 'This is the time (in seconds) between each update of the monitors, 0 means no refresh',
      type: 'slider',
      attrs: {
        min: 0,
        max: 5,
        step: 0.25,
      },
      defaultValue: this.defaultRate,
      onChange: async(value: string) => {
        let valueNumber: number;

        try {
          valueNumber = parseFloat(value);
          if (isNaN(valueNumber)) {
            throw new Error('invalid value');
          }
        } catch (error) {
          console.error(error);
          return;
        }
        try {
          await this.updateServer({
            rate: valueNumber,
          });
        } catch (error) {
          console.error(error);
          return;
        }

        if (valueNumber === 0) {
          this.updateAllMonitors({
            cpu_utilization: 0,
            device: 'cpu',

            gpus: [
              {
                gpu_utilization: 0,
                gpu_temperature: 0,
                vram_total: 0,
                vram_used: 0,
                vram_used_percent: 0,
              },
            ],
            hdd_total: 0,
            hdd_used: 0,
            hdd_used_percent: 0,
            ram_total: 0,
            ram_used: 0,
            ram_used_percent: 0,
          });
        }

        this.updateAllAnimationDuration(valueNumber);
      },
    });

    void this.getHDDsFromServer().then((data: string[]): void => {
      const which = app.ui.settings.getSettingValue(this.idWhichHDD, this.defaultWhichHDD);
      app.ui.settings.addSetting({
        id: this.idWhichHDD,
        name: this.menuPrefix + '[monitor] Partition to show',
        type: 'combo',
        defaultValue: this.defaultWhichHDD,
        // @ts-ignore bad definition from quasarUI: `options?: undefined;`??
        options: (value: string) =>
          data.map((m) => ({
            value: m,
            text: m,
            selected: !value ? m === which : m === value,
          })),
        onChange: async(value: string) => {
          await this.updateServer({
            whichHDD: value,
          });
        },
      });
    });

    void this.getGPUsFromServer().then((gpus: TGpuName[]): void => {
      let moreThanOneGPU = false;
      if (gpus.length > 1) {
        moreThanOneGPU = true;
      }

      gpus?.forEach(({
        name, index
      }) => {

        if(name === undefined || index === undefined) {
          console.warn('getGPUsFromServer: name or index undefined', name, index);
          return;
        }

        let label = 'GPU';
        let labelVRAM = 'VRAM';
        let labelTemperature = 'Temp';
        if (moreThanOneGPU) {
          label = 'GPU '+index;
          labelVRAM = 'VRAM'+index;
          labelTemperature = 'Temp '+index;
        }

        // GPU Utilization Variables
        const monitorGPUNElement: TMonitorSettings = {
          id: 'Crystools.switchGPU' + index,
          name: this.menuPrefix + `[menu] Display GPU\r\n[${index}] ${name}`,
          type: 'boolean',
          label,
          symbol: '%',
          title: `${index}: ${name}`,
          defaultValue: true,
          htmlMonitorRef: undefined,
          htmlMonitorSliderRef: undefined,
          htmlMonitorLabelRef: undefined,
          cssColor: '#0C86F4',
          onChange: async(value: boolean) => {
            this.updateWidget(monitorGPUNElement);
            void await this.updateServerGPU(index,{
              utilization: value
            });
          },
        };

        // GPU VRAM Variables
        const monitorVRAMNElement: TMonitorSettings = {
          id: 'Crystools.switchVRAM' + index,
          name: this.menuPrefix + `[menu] Display GPU VRAM\r\n[${index}] ${name}`,
          type: 'boolean',
          label: labelVRAM,
          symbol: '%',
          title: `${index}: ${name}`,
          defaultValue: true,
          htmlMonitorRef: undefined,
          htmlMonitorSliderRef: undefined,
          htmlMonitorLabelRef: undefined,
          cssColor: '#176EC7',
          onChange: async(value: boolean) => {
            this.updateWidget(monitorVRAMNElement);
            void await this.updateServerGPU(index,{
              vram: value
            });
          },
        };

        // GPU Temperature Variables
        const monitorTemperatureNElement: TMonitorSettings = {
          id: 'Crystools.switchTemperature' + index,
          name: this.menuPrefix + `[menu] Display GPU Temperature\r\n[${index}] ${name}`,
          type: 'boolean',
          label: labelTemperature,
          symbol: '°',
          title: `${index}: ${name}`,
          defaultValue: true,
          htmlMonitorRef: undefined,
          htmlMonitorSliderRef: undefined,
          htmlMonitorLabelRef: undefined,
          cssColor: '#00ff00',
          cssColorFinal: '#ff0000',
          onChange: async(value: boolean) => {
            this.updateWidget(monitorTemperatureNElement);
            void await this.updateServerGPU(index,{
              temperature: value
            });
          },
        };

        this.monitorGPUSettings[index] = monitorGPUNElement;
        this.monitorVRAMSettings[index] = monitorVRAMNElement;
        this.monitorTemperatureSettings[index] = monitorTemperatureNElement;
        // @ts-ignore
        app.ui.settings.addSetting(this.monitorGPUSettings[index]);
        // @ts-ignore
        app.ui.settings.addSetting(this.monitorVRAMSettings[index]);
        // @ts-ignore
        app.ui.settings.addSetting(this.monitorTemperatureSettings[index]);
      });
    });
  };


  updateServer = async(data: TStatsSettings): Promise<string> => {
    const resp = await api.fetchApi('/crystools/monitor', {
      method: 'PATCH',
      body: JSON.stringify(data),
      cache: 'no-store',
    });
    if (resp.status === 200) {
      return await resp.text();
    }
    throw new Error(resp.statusText);
  };

  updateServerGPU = async(index: number, data: TGpuSettings): Promise<string> => {
    const resp = await api.fetchApi(`/crystools/monitor/GPU/${index}`, {
      method: 'PATCH',
      body: JSON.stringify(data),
      cache: 'no-store',
    });
    if (resp.status === 200) {
      return await resp.text();
    }
    throw new Error(resp.statusText);
  };

  getHDDsFromServer = async(): Promise<string[]> => {
    return this.getDataFromServer('HDD');
  };

  getGPUsFromServer = async(): Promise<TGpuName[]> => {
    return this.getDataFromServer<TGpuName>('GPU');
  };

  getDataFromServer = async<T>(what: string): Promise<T[]> => {
    const resp = await api.fetchApi(`/crystools/monitor/${what}`, {
      method: 'GET',
      cache: 'no-store',
    });
    if (resp.status === 200) {
      return await resp.json();
    }
    throw new Error(resp.statusText);
  };

  updateAllWidget = (): void => {
    this.updateWidget(this.monitorCPUElement);
    this.updateWidget(this.monitorRAMElement);
    this.updateWidget(this.monitorHDDElement);

    this.monitorGPUSettings.forEach((monitorSettings) => {
      monitorSettings && this.updateWidget(monitorSettings);
    });
    this.monitorVRAMSettings.forEach((monitorSettings) => {
      monitorSettings && this.updateWidget(monitorSettings);
    });
    this.monitorTemperatureSettings.forEach((monitorSettings) => {
      monitorSettings && this.updateWidget(monitorSettings);
    });
  };

  updateWidget = (monitorSettings: TMonitorSettings): void => {
    const value = app.ui.settings.getSettingValue(monitorSettings.id, monitorSettings.defaultValue);
    if (monitorSettings.htmlMonitorRef) {
      monitorSettings.htmlMonitorRef.style.display = value ? 'flex' : 'none';
    }
  };


  updateAllMonitors = (data: TStatsData): void => {
    // console.log('updateAllMonitors', data);
    this.updateMonitor(this.monitorCPUElement, data.cpu_utilization);
    this.updateMonitor(this.monitorRAMElement, data.ram_used_percent);
    this.updateMonitor(this.monitorHDDElement, data.hdd_used_percent);

    if (data.gpus === undefined || data.gpus.length === 0) {
      console.warn('UpdateAllMonitors: no GPU data');
      return;
    }

    this.monitorGPUSettings.forEach((monitorSettings, index) => {
      if (data.gpus[index]) {
        const gpu = data.gpus[index];
        if (gpu === undefined) {
          // console.error('UpdateAllMonitors: no GPU data for index', index);
          return;
        }

        this.updateMonitor(monitorSettings, gpu.gpu_utilization);
      } else {
        // console.error('UpdateAllMonitors: no GPU data for index', index);
      }
    });

    this.monitorVRAMSettings.forEach((monitorSettings, index) => {
      if (data.gpus[index]) {
        const gpu = data.gpus[index];
        if (gpu === undefined) {
          // console.error('UpdateAllMonitors: no GPU VRAM data for index', index);
          return;
        }

        this.updateMonitor(monitorSettings, gpu.vram_used_percent);
      } else {
        // console.error('UpdateAllMonitors: no GPU VRAM data for index', index);
      }
    });

    this.monitorTemperatureSettings.forEach((monitorSettings, index) => {
      if (data.gpus[index]) {
        const gpu = data.gpus[index];
        if (gpu === undefined) {
          // console.error('UpdateAllMonitors: no GPU VRAM data for index', index);
          return;
        }

        this.updateMonitor(monitorSettings, gpu.gpu_temperature);
        if(monitorSettings.cssColorFinal && monitorSettings.htmlMonitorSliderRef){
          monitorSettings.htmlMonitorSliderRef.style.backgroundColor =
            `color-mix(in srgb, ${monitorSettings.cssColorFinal} ${gpu.gpu_temperature}%, ${monitorSettings.cssColor})`;
        }
      } else {
        // console.error('UpdateAllMonitors: no GPU VRAM data for index', index);
      }
    });
  };

  updateMonitor = (monitorSettings: TMonitorSettings, percent: number): void => {
    if (!(monitorSettings.htmlMonitorSliderRef && monitorSettings.htmlMonitorLabelRef)) {
      return;
    }

    monitorSettings.htmlMonitorLabelRef.innerHTML = `${Math.floor(percent)}${monitorSettings.symbol}`;
    monitorSettings.htmlMonitorSliderRef.style.width = `${Math.floor(percent)}%`;
  };

  updateAllAnimationDuration = (value: number): void => {
    this.updatedAnimationDuration(this.monitorCPUElement, value);
    this.updatedAnimationDuration(this.monitorRAMElement, value);
    this.updatedAnimationDuration(this.monitorHDDElement, value);
    this.monitorGPUSettings.forEach((monitorSettings) => {
      monitorSettings && this.updatedAnimationDuration(monitorSettings, value);
    });
    this.monitorVRAMSettings.forEach((monitorSettings) => {
      monitorSettings && this.updatedAnimationDuration(monitorSettings, value);
    });
    this.monitorTemperatureSettings.forEach((monitorSettings) => {
      monitorSettings && this.updatedAnimationDuration(monitorSettings, value);
    });
  };

  updatedAnimationDuration = (monitorSettings: TMonitorSettings, value: number): void => {
    const slider = monitorSettings.htmlMonitorSliderRef;
    if (!slider) {
      return;
    }

    slider.style.transition = `width ${value.toFixed(1)}s`;
  };

  setup(): void {
    const parentElement = document.getElementById('queue-button');

    let ctoolsRoot = document.getElementById(this.htmlIdCrystoolsRoot);
    if (!ctoolsRoot) {
      ctoolsRoot = document.createElement('div');
      ctoolsRoot.setAttribute('id', this.htmlIdCrystoolsRoot);
      ctoolsRoot.style.display = 'flex';
      ctoolsRoot.style.width = '100%';
      ctoolsRoot.style.flexDirection = 'column';
      parentElement?.insertAdjacentElement('afterend', ctoolsRoot);
    }

    const htmlContainer = document.createElement('div');
    htmlContainer.setAttribute('id', this.htmlIdCrystoolsMonitorContainer);
    htmlContainer.style.width = '100%';
    htmlContainer.style.cursor = 'crosshair';
    htmlContainer.style.order = '3';
    htmlContainer.style.margin = '4px 0';
    ctoolsRoot.append(htmlContainer);

    htmlContainer.append(this.createMonitor(this.monitorCPUElement));
    htmlContainer.append(this.createMonitor(this.monitorRAMElement));

    // gpu0 > gpu1 > vram0 > vram1
    // this.monitorGPUSettings.forEach((monitorSettings) => {
    //   monitorSettings && htmlContainer.append(this.createMonitor(monitorSettings));
    // });
    // this.monitorVRAMSettings.forEach((monitorSettings) => {
    //   monitorSettings && htmlContainer.append(this.createMonitor(monitorSettings));
    // });
    // this.monitorTemperatureSettings.forEach((monitorSettings) => {
    //   monitorSettings && htmlContainer.append(this.createMonitor(monitorSettings));
    // });

    // gpu0 > vram0 > gpu1 > vram1
    this.monitorGPUSettings.forEach((_monitorSettings, index) => {
      this.monitorGPUSettings[index] && htmlContainer.append(this.createMonitor(this.monitorGPUSettings[index]));
      this.monitorVRAMSettings[index] && htmlContainer.append(this.createMonitor(this.monitorVRAMSettings[index]));
      this.monitorTemperatureSettings[index] &&
        htmlContainer.append(this.createMonitor(this.monitorTemperatureSettings[index]));
    });

    htmlContainer.append(this.createMonitor(this.monitorHDDElement));

    const currentRate = parseFloat(app.ui.settings.getSettingValue(this.idInputRate, this.defaultRate));
    this.updateAllAnimationDuration(currentRate);
    this.updateAllWidget();
    this.registerListeners();
  }

  createMonitor = (monitorSettings?: TMonitorSettings): HTMLDivElement => {
    if (!monitorSettings) {
      // just for typescript
      return document.createElement('div');
    }
    const htmlMain = document.createElement('div');
    htmlMain.setAttribute('id', monitorSettings.id);
    htmlMain.style.margin = '2px 10px';
    htmlMain.style.height = '12px';
    htmlMain.style.position = 'relative';
    htmlMain.style.display = 'flex';
    htmlMain.style.alignItems = 'center';
    htmlMain.style.flexDirection = 'row';
    monitorSettings.htmlMonitorRef = htmlMain;

    if (monitorSettings.title) {
      htmlMain.title = monitorSettings.title;
    }

    const htmlMonitorText = document.createElement('div');
    htmlMonitorText.style.width = '35px';
    htmlMonitorText.style.fontSize = '10px';
    htmlMonitorText.innerHTML = monitorSettings.label;
    htmlMain.append(htmlMonitorText);

    const htmlMonitorContent = document.createElement('div');
    htmlMonitorContent.style.height = '100%';
    htmlMonitorContent.style.flexGrow = '1';
    htmlMonitorContent.style.position = 'relative';
    htmlMonitorContent.style.backgroundColor = 'var(--bg-color)';
    htmlMain.append(htmlMonitorContent);

    const htmlMonitorSlider = document.createElement('div');
    htmlMonitorSlider.style.position = 'absolute';
    htmlMonitorSlider.style.height = '100%';
    htmlMonitorSlider.style.width = '0';
    if(monitorSettings.cssColorFinal){
      htmlMonitorSlider.style.backgroundColor =
        `color-mix(in srgb, ${monitorSettings.cssColorFinal} 0%, ${monitorSettings.cssColor})`;
    } else {
      htmlMonitorSlider.style.backgroundColor = monitorSettings.cssColor;
    }
    monitorSettings.htmlMonitorSliderRef = htmlMonitorSlider;
    htmlMonitorContent.append(htmlMonitorSlider);

    const htmlMonitorLabel = document.createElement('div');
    htmlMonitorLabel.style.position = 'relative';
    htmlMonitorLabel.style.width = '100%';
    htmlMonitorLabel.style.color = 'var(--drag-text)';
    htmlMonitorLabel.style.fontSize = '10px';
    htmlMonitorLabel.innerHTML = '0%';
    monitorSettings.htmlMonitorLabelRef = htmlMonitorLabel;
    htmlMonitorContent.append(htmlMonitorLabel);

    return monitorSettings.htmlMonitorRef;
  };

  registerListeners = (): void => {
    api.addEventListener('crystools.monitor', (event: CustomEvent) => {
      if (event?.detail === undefined) {
        return;
      }
      this.updateAllMonitors(event.detail);
    }, false);
  };
}

const crystoolsMonitor = new CrystoolsMonitor();
app.registerExtension({
  name: crystoolsMonitor.idExtensionName,
  setup: crystoolsMonitor.setup.bind(crystoolsMonitor),
});
