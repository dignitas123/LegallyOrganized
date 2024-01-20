<template>
  <div>
    <q-table
      class="q-my-md"
      :rows="legalRequests"
      row-key="id"
      :columns="columns"
    >
      <template v-slot:body-cell-status="props">
        <!-- Display a dropdown for status updates -->
        <q-select
          v-model="props.row.status"
          :options="statusOptions"
          emit-value
          map-options
          @input="updateStatus(props.row)"
        />
      </template>
      <template v-slot:top-right>
        <!-- Add any additional controls or filters here -->
      </template>
    </q-table>

    <div class="create-button-container fixed-bottom q-mb-lg">
      <q-btn
        class="create-button"
        label="Create New Legal Request"
        color="secondary"
        @click="redirectToSubmitRequest"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { LegalRequestStatus } from 'src/interfaces/legal-request'
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

function redirectToSubmitRequest() {
  router.push({ name: 'submit-request' });
}

const legalRequests = ref([]);
const columns = ref([
  { name: 'id', required: true, label: 'ID', align: 'left', field: 'id' },
  { name: 'clientName', label: 'Client Name', align: 'left', field: 'clientName' },
  { name: 'caseDescription', label: 'Case Description', align: 'left', field: 'caseDescription' },
  { name: 'status', required: true, label: 'Status', align: 'left', field: 'status' },
  // Add more columns as needed
]);
const statusOptions = ref(['Open', 'In Progress', 'Completed', 'Rejected']);

onMounted(async () => {
  // Fetch legal requests data from Django backend
  await fetchLegalRequests();
});

async function fetchLegalRequests() {
  try {
    const response = await axios.get('http://localhost:8000/api/legal_requests/');
    legalRequests.value = response.data;
  } catch (error) {
    console.error('Error fetching legal requests:', error);
  }
}

async function updateStatus(legalRequest: { id: string; status: LegalRequestStatus; }) {
  try {
    await axios.put(`http://localhost:8000/api/legal_requests/${legalRequest.id}/`, {
      status: legalRequest.status,
    });
  } catch (error) {
    console.error('Error updating status:', error);
  }
}
</script>

<style scoped lang="scss">
.container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Set the container to full viewport height */
}

.spacer {
  flex: 1; /* Grow and push the button to the bottom */
}

.create-button-container {
  display: flex;
  justify-content: center;
}

.create-button {
  font-size: 18px;
  padding: 15px 30px;
  border-radius: 30px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.create-button:hover {
  background-color: #007bff; /* Change to your desired hover color */
  color: #fff;
}
</style>
