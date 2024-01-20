<template>
  <q-page padding>
    <q-form @submit.prevent="onSubmit" class="q-gutter-md">
      <q-input filled v-model="client.name" label="Client Name" :rules="[val => !!val || 'Field is required']" />
      <q-input filled v-model="client.email" label="Email" :rules="[val => !!val || 'Field is required']" />
      <q-input filled v-model="client.phone" label="Phone" :rules="[val => !!val || 'Field is required']" />
      <q-input type="textarea" filled v-model="legalRequest.caseDescription" label="Case Description" :rules="[val => !!val || 'Field is required']" />
      <q-select filled v-model="legalRequest.caseType" :options="caseTypes" label="Case Type" :rules="[val => !!val || 'Field is required']" />
      <q-file filled v-model="documents" label="Document Attachments" multiple />
      <q-btn label="Submit" type="submit" color="secondary" />
    </q-form>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import { Notify } from 'quasar';

interface Client {
  name: string;
  email: string;
  phone: string;
}

interface LegalRequest {
  caseDescription: string;
  caseType: string;
  client: number | null;
}

const client = ref<Client>({
  name: '',
  email: '',
  phone: ''
});

const legalRequest = ref<LegalRequest>({
  caseDescription: '',
  caseType: '',
  client: null
});

const caseTypes = ref(['Type 1', 'Type 2', 'Type 3']); // Example case types

const documents = ref<File[]>([]);

const onSubmit = async () => {
  try {
    // Step 1: Create the client
    const clientResponse = await axios.post('http://localhost:8000/api/clients/', client.value);
    const clientId = clientResponse.data.id;

    // Step 2: Create the legal request
    legalRequest.value.client = clientId;
    const requestResponse = await axios.post('http://localhost:8000/api/legal_requests/', legalRequest.value);
    const requestId = requestResponse.data.id;

    // Step 3: Upload documents
    const formData = new FormData();
    documents.value.forEach((document, index) => {
      formData.append(`documents[${index}]`, document);
    });
    await axios.post(`http://localhost:8000/api/document_attachments/?legal_request_id=${requestId}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    Notify.create('Legal request submitted successfully');
  } catch (error: any) {
    if (axios.isAxiosError(error) && error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.error('Error Response', error.response.data);
      console.error('Error Status', error.response.status);
      console.error('Error Headers', error.response.headers);
    } else if (error.request) {
      // The request was made but no response was received
      console.error('Error Request', error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('Error Message', error.message);
    }
    console.error('Error submitting legal request', error);
    Notify.create(`Error submitting legal request ${error.message}`);
  }
};
</script>
