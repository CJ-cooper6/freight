import axios from 'axios';

const apiBaseUrl = 'http://localhost:5000/api'

axios.defaults.withCredentials = true;

export default {
    getData(pageSize, currentPage) {
        return axios.get(`${apiBaseUrl}/freight`, {
          params: { 
            pageSize,
            currentPage,
          },
        });
      },
};