## Шаг 1: Установка Docker
1.1. Удаление старых версий
Если у вас уже установлены старые версии Docker, удалите их:
```
sudo apt-get remove docker docker-engine docker.io containerd runc
```

1.2. Установка необходимых пакетов
Установите пакеты, необходимые для установки Docker:
```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

1.3. Добавление официального GPG ключа Docker
Добавьте ключ GPG Docker:
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

1.4. Добавление Docker репозитория
Добавьте Docker репозиторий в список источников APT:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```

1.5. Установка Docker Engine
Обновите список пакетов и установите Docker Engine:
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

1.6. Проверка установки
Проверьте установку Docker, запустив тестовый контейнер:
```
sudo docker run hello-world
```

## Шаг 2: Установка Docker Compose
2.1. Загрузка Docker Compose
Загрузите последнюю версию Docker Compose:
```
DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4)
sudo curl -L "https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

2.2. Установка разрешений
Сделайте Docker Compose исполняемым:
```
sudo chmod +x /usr/local/bin/docker-compose
```

2.3. Проверка установки
Проверьте установку Docker Compose:
```
docker-compose --version
```

## Шаг 3: Настройка прав доступа (опционально)
Добавьте вашего пользователя в группу docker, чтобы запускать Docker без sudo:
```
sudo usermod -aG docker $USER
```
Перезагрузите систему или выйдите из текущей сессии и снова войдите, чтобы изменения вступили в силу.

Теперь Docker и Docker Compose установлены и готовы к использованию на вашем сервере.