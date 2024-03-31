<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const Logout = () => {
    localStorage.clear();
    router.push('/');
};

onMounted(() => {
    Logout();
});
</script>
