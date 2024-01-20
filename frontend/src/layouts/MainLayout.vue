<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-icon name="img:icons/favicon-96x96.png" size="md" />
        <q-toolbar-title class="text-black">
          Legally Organized
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container class="q-pa-md">
    <q-breadcrumbs class="q-my-md" v-if="route.path !== '/'">
      <q-breadcrumbs-el
        class="text-black"
        v-for="(breadcrumb, index) in breadcrumbs"
        :key="index"
        :label="breadcrumb.label"
        :icon="breadcrumb.icon"
        :to="breadcrumb.to"
      />
    </q-breadcrumbs>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const capitalizeFirstLetter = (string: string) => {
  return string
    .toLowerCase()
    .replace(/-/g, ' ')
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
};

const breadcrumbs = computed(() => {
  const routes = route.matched;
  return routes.map((r, index) => {
    // Ensure label is a string
    let label = '';
    if (typeof r.meta.title === 'string') {
      label = r.meta.title;
    } else if (typeof r.name === 'string') {
      label = r.name;
    }

    label = index === 0 && label === '' ? 'Dashboard' : capitalizeFirstLetter(label);
    return {
      label: label,
      icon: index === 0 ? 'dashboard' : undefined,
      to: r.path
    };
  });
});
</script>
