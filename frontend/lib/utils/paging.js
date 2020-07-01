// from next-realworld-app
const paging = (limit, page) =>
  `limit=${limit}&offset=${page ? page * limit : 0}`;

export default paging;
