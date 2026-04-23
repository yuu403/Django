# Task Management App (Django)

## 概要

Djangoで作成したシンプルなタスク管理アプリです。
ユーザー認証機能を含み、ログインしたユーザーごとにタスクを管理できます。

---

## 主な機能

* ユーザー登録
* ログイン / ログアウト
* タスクの作成
* タスクの一覧表示
* タスクの詳細表示
* タスクの更新
* タスクの削除

---

## 使用技術

* Python
* Django
* HTML / CSS
* SQLite（デフォルトDB）

---

## 画面構成

* トップページ（タスク一覧）
* ログインページ
* ユーザー登録ページ
* タスク作成ページ
* タスク詳細ページ
* タスク編集ページ

---

## ディレクトリ構成（抜粋）

```
taskproject/
├── taskproject/
│   ├── settings.py
│   ├── urls.py
│
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── registration
│   ├── tasks/
│
├── manage.py
```

---

## URL設計（例）

* `/` : タスク一覧
* `/login/` : ログイン
* `/logout/` : ログアウト
* `/signup/` : ユーザー登録
* `/create/` : タスク作成
* `/detail/<int:pk>/` : タスク詳細
* `/update/<int:pk>/` : タスク更新
* `/delete/<int:pk>/` : タスク削除

---

## セットアップ方法

### 1. リポジトリをクローン

```
git clone <リポジトリURL>
cd taskproject
```

### 2. 仮想環境を作成・有効化

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. パッケージをインストール

```
pip install django
```

### 4. マイグレーション

```
python manage.py makemigrations
python manage.py migrate
```

### 5. サーバー起動

```
python manage.py runserver
```

---

## 今後の改善点

* UIの改善（Bootstrapなど導入）
* 検索機能の追加
* タスクのカテゴリ分け
* 期限や優先度の追加
* デプロイ（Render / Railway など）

---

## 学習ポイント

* DjangoのMTV構造の理解
* 認証機能（LoginView / LogoutView / UserCreationForm）
* URLルーティングの整理（プロジェクトとアプリの違い）
* テンプレート継承（base.html）
* CRUD処理の実装

---
## 開発で苦労した点

* 認証機能の実装（LoginView / LogoutView / UserCreationFormの連携）
* URL設計（プロジェクト側とアプリ側の役割の違い）
* TemplateDoesNotExistエラーの解決（テンプレート配置とsettingsの理解）

## 工夫した点

* ユーザーごとにタスクを分離する設計
* テンプレート継承（base.html）による共通化
* シンプルなCRUD構成で可読性を重視

## 今後の課題

* UI/UXの改善
* 機能追加（検索・カテゴリ・期限）
* 本番環境へのデプロイ


## 補足

このアプリはDjangoの基礎学習およびポートフォリオ作成を目的として作成しています。
