import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightThemeNext from 'starlight-theme-next';
import mermaid from 'astro-mermaid';

export default defineConfig({
  site: 'https://atoom74.github.io',
  base: '/esphome-bthome',
  integrations: [
    mermaid({
      theme: 'neutral',
      autoTheme: true,
    }),
    starlight({
      plugins: [starlightThemeNext()],
      title: 'BTHome for ESPHome (nRF52 fork)',
      description: 'BTHome v2 BLE Protocol Component for ESPHome',
      social: [
          { icon: 'github', label: 'GitHub', href: 'https://github.com/AToom74/esphome-bthome' },
        ],
      expressiveCode: {
        themes: ['github-dark', 'github-light'],
        defaultProps: {
          wrap: true,
        },
        styleOverrides: {
          borderRadius: '0.5rem',
          codePaddingBlock: '0.75rem',
          codePaddingInline: '1rem',
        },
      },
      sidebar: [
        {
          label: 'Getting Started',
          items: [{ autogenerate: { directory: 'getting-started' } }],
        },
        {
          label: 'Configuration',
          items: [{ autogenerate: { directory: 'configuration' } }],
        },
        {
          label: 'Components',
          items: [{ autogenerate: { directory: 'components' } }],
        },
        {
          label: 'Platforms',
          items: [{ autogenerate: { directory: 'platforms' } }],
        },
        {
          label: 'Devices',
          items: [{ autogenerate: { directory: 'devices' } }],
        },
        {
          label: 'Reference',
          items: [{ autogenerate: { directory: 'reference' } }],
        },
      ],
      editLink: {
          baseUrl: 'https://github.com/AToom74/esphome-bthome/edit/main/docs/',
        },
    }),
  ],
});
