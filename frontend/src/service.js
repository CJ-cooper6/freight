import axios from 'axios';

const apiBaseUrl = '/api'

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
    
    saveData(id, data) {
      console.log(data)
      return axios.put(`${apiBaseUrl}/freight/${id}`,data);
    },
};