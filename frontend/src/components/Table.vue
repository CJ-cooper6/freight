<template>
  <div>
    <a-button
      class="editable-add-btn"
      style="margin-bottom: 8px"
      @click="handleAdd"
      >添加</a-button
    >
    <a-table
      :columns="columns"
      :data-source="dataSource"
      :pagination="false"
      :size="small"
      :scroll="{ x: 600 }"
      bordered
    >
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
              class="my-custom-input"
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
              <a-popconfirm
                title="确定删除?"
                ok-text="确定"
                cancel-text="取消"
                @confirm="onDelete(record.id)"
              >
                <a>删除</a>
              </a-popconfirm>
            </span>
          </div>
        </template>
      </template>
    </a-table>
    <div class="pagination">
      <a-pagination
        v-model:current="pagination.current"
        v-model:pageSize="pagination.pageSize"
        :total="pagination.total"
        :showSizeChanger="true"
        :pageSizeOptions="['5', '10', '20']"
        @change="fetchData()"
      />
    </div>
  </div>
</template>
<script setup>
import { cloneDeep } from "lodash-es";
import { reactive, ref, onMounted, computed } from "vue";
import Service from "../service";

const setRowClassName = () => {
  return 'custom-row'; 
};

const columns = [
  {
    title: "日期",
    dataIndex: "date",
    width:50,
  },
  {
    title: "货号",
    dataIndex: "number",
    width:50,
  },
  {
    title: "品名",
    dataIndex: "name",
    width:50,
  },
  {
    title: "长",
    dataIndex: "long",
    width:25,
  },
  {
    title: "宽",
    dataIndex: "width",
    width:25,
  },
  {
    title: "高",
    dataIndex: "hight",
    width:25,
  },
  {
    title: "件数",
    dataIndex: "piece",
    width:35,
  },
  {
    title: "立方",
    dataIndex: "cube",
    width:30,
  },
  {
    title: "重量",
    dataIndex: "weight",
    width:30,
  },
  {
    title: "垫付款",
    dataIndex: "imprest",
    width:40,
  },
  {
    title: "包装数",
    dataIndex: "package_number",
    width:50,
  },
  {
    title: "房间",
    dataIndex: "room",
    width:50,
  },
  {
    title: "操作",
    dataIndex: "operation",
  },
];

const data = ref([]);
const dataSource = ref(data);
const editableData = reactive({});

const pagination = reactive({
  pageSize: 10, // 每页显示的数量
  current: 1, // 当前页码
  total: 0,
});

const first_id = computed(() =>
  dataSource.value[0] ? dataSource.value[0].id + 1 : 0
);

const fetchData = () => {
  Service.getData(pagination.pageSize, pagination.current)
    .then((response) => {
      data.value = response.data.freight_items;
      pagination.total = response.data.total;
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

    //取消所有编辑状态
    const keys = Object.keys(editableData);
    keys.forEach((key) => {
      delete editableData[key];
    });

    fetchData();
  });
};

const cancel = (id) => {
  delete editableData[id];
};

const handleAdd = () => {
  const new_id = first_id.value;
  const newData = {
    id: new_id,
  };
  dataSource.value.unshift(newData);
  editableData[new_id] = cloneDeep(newData);
};

const onDelete = (id) => {
  Service.deleteData(id).then((response) => {
    fetchData();
  });
};

onMounted(() => {
  fetchData();
});

function customRowClassName(record, index) {
  return 'row-class';
}

</script>
<style scoped>
.editable-row-operations a {
  margin-right: 8px;
}
.editable-add-btn {
  margin-bottom: 8px;
}

.pagination {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

.row-class {
  height: 10px; 
}

/deep/ .ant-table-tbody > tr > td {
  padding: 2px;
}

/deep/ .ant-table-thead > tr > th {
  padding: 2px;
}

::v-deep .ant-table-tbody > tr > td {
  font-size: 9px;
}

::v-deep .ant-table-thead > tr > th  {
  font-size: 10px;
}

.my-custom-input {
  margin: -5px 0;
  padding: 0;
  border-radius: 3px;
  font-size: 10px;
}

.popconfirm {
  font-size: 10px;
}

</style>