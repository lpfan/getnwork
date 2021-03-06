import CategoryList from './components/CategoryList.vue';
import CategoryPostList from './components/CategoryPostList.vue';
import PostDetail from './components/PostDetail.vue';
import MainPage from './components/MainPage.vue';

export const routes = [
  { path: '', component: MainPage, name: 'mainPage'},
  { path: '/categories/', component: CategoryList},
  { path: '/categories/:category_slug/posts/', component: CategoryPostList, name: 'categoriesposts' },
  { path: '/categories/:category_slug/posts/:post_slug/', component: PostDetail}
];
