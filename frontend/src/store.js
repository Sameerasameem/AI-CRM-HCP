import { configureStore, createSlice } from "@reduxjs/toolkit";

const crmSlice = createSlice({
  name: "crm",
  initialState: {
    reply: "",
  },
  reducers: {
    setReply: (state, action) => {
      state.reply = action.payload;
    },
  },
});

export const { setReply } = crmSlice.actions;

export const store = configureStore({
  reducer: {
    crm: crmSlice.reducer,
  },
});