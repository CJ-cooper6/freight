<template>
  <div>
    <a-table :columns="columns" :data-source="dataSource" bordered>
      <template #bodyCell="{ column, text, record }">
        <template
          v-if="
            [
              'date',
              'number',
              'name',
              'piece',
              'cube',
              'piece',
              'weight',
              'imprest',
              'package_number',
              'room',
            ].includes(column.dataIndex)
          "
        >
          <div>
            <a-input
              v-if="editableData[record.id]"
              v-model:value="editableData[record.id][column.dataIndex]"
              style="margin: -5px 0"
            />
            <template v-else>
              {{ text }}
            </template>
          </div>
        </template>
        <template v-else-if="column.dataIndex === 'operation'">
          <div class="editable-row-operations">
            <span v-if="editableData[record.id]">
              <a-typography-link @click="save(record.id)"
                >保存</a-typography-link
              >
              <a-typography-link title="确定取消?" @click="cancel(record.id)">
                <a>取消</a>
              </a-typography-link>
            </span>
            <span v-else>
              <a @click="edit(record.id)">编辑</a>
            </span>
          </div>
        </template>
      </template>
    </a-table>
    <a-button
      class="editable-add-btn"
      style="margin-bottom: 8px"
      @click="handleAdd"
      >Add</a-button
    >
  </div>
</template>
<script setup>
import { cloneDeep } from "lodash-es";
import { reactive, ref, onMounted } from "vue";
import Service from "../service";

const columns = [
  {
    title: "日期",
    dataIndex: "date",
    width: "10%",
  },
  {
    title: "货号",
    dataIndex: "number",
    width: "10%",
  },
  {
    title: "品名",
    dataIndex: "name",
    width: "10%",
  },
  {
    title: "件数",
    dataIndex: "piece",
    width: "10%",
  },
  {
    title: "立方",
    dataIndex: "cube",
    width: "10%",
  },
  {
    title: "重量",
    dataIndex: "weight",
    width: "10%",
  },
  {
    title: "垫付款",
    dataIndex: "imprest",
    width: "10%",
  },
  {
    title: "包装数",
    dataIndex: "package_number",
    width: "10%",
  },
  {
    title: "房间",
    dataIndex: "room",
    width: "10%",
  },
  {
    title: "操作",
    dataIndex: "operation",
  },
];

const data = ref([]);
const dataSource = ref(data);
const editableData = reactive({});

const total = ref(0);
const pagination = reactive({
  pageSize: 10, // 每页显示的数量
  currentPage: 1, // 当前页码
});

const fetchData = () => {
  Service.getData(pagination.pageSize, pagination.currentPage)
    .then((response) => {
      data.value = response.data.freight_items;
      total.value = data.total;
    })
    .catch((error) => {
      console.error("获取失败:", error);
    });
};

const edit = (id) => {
  editableData[id] = cloneDeep(
    dataSource.value.filter((item) => id === item.id)[0]
  );
};

const save = (id) => {
  Service.saveData(id, editableData[id]).then((response) => {
    Object.assign(
      dataSource.value.filter((item) => id === item.id)[0],
      editableData[id]
    );
    delete editableData[id];
  });
};

const cancel = (id) => {
  delete editableData[id];
};

onMounted(() => {
  fetchData();
});
</script>
<style scoped>
.editable-row-operations a {
  margin-right: 8px;
}
.editable-add-btn {
  margin-bottom: 8px;
}
</style>