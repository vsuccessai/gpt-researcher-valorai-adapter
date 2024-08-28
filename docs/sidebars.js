/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

 module.exports = {
  docsSidebar: [
    'welcome',
    {
      type: 'category',
      label: 'Getting Started',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/getting-started/introduction',
        'gpt-researcher/getting-started/getting-started-with-docker',
        'gpt-researcher/getting-started/getting-started',
        'gpt-researcher/getting-started/linux-deployment',
      ]
    },
    {
      type: 'category',
      label: 'GPT Researcher',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/gptr/pip-package',
        'gpt-researcher/gptr/example',
        'gpt-researcher/gptr/automated-tests',
        'gpt-researcher/gptr/troubleshooting',
      ],
    },

    {
      type: 'category',
      label: 'Frontend',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/frontend/frontend',
        'gpt-researcher/frontend/playing-with-webhooks',
      ],
    },
    
    
    {
      type: 'category',
      label: 'Custom Context',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/context/tailored-research',
        'gpt-researcher/context/local-docs',
        'gpt-researcher/context/vector-stores',
        ]
    },
    {
      type: 'category',
      label: 'Large Language Models',
      collapsible: true,
      collapsed: false,
      items: [
        'gpt-researcher/llms/llms',
        'gpt-researcher/llms/deploy-llm-on-elestio.md'
      ]
    },
    
    {
      type: 'category',
      label: 'More Customization',
      collapsible: true,
      collapsed: true,
      items: [
        'gpt-researcher/customization/config',
        'gpt-researcher/customization/retrievers',
        ]
    },
    {
      type: 'category',
      label: 'Multi-Agent Frameworks',
      collapsible: true,
      collapsed: true,
      items: [
        'gpt-researcher/multi_agents/langgraph',
        ]
    },
    {'Examples': [{type: 'autogenerated', dirName: 'examples'}]},
    'contribute',
    'roadmap',
  ],
  // pydoc-markdown auto-generated markdowns from docstrings
  referenceSideBar: [require("./docs/reference/sidebar.json")]
};
